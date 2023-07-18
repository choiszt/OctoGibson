from IPython import embed

import omnigibson as og
from omnigibson.object_states.aabb import AABB
from omnigibson.object_states.adjacency import HorizontalAdjacency, VerticalAdjacency, flatten_planes
from omnigibson.object_states.kinematics import KinematicsMixin
from omnigibson.object_states.object_state_base import BooleanState, RelativeObjectState
from omnigibson.utils.object_state_utils import sample_kinematics
from omnigibson.utils.usd_utils import BoundingBoxAPI


class Inside(KinematicsMixin, RelativeObjectState, BooleanState):
    @staticmethod
    def get_dependencies():
        return KinematicsMixin.get_dependencies() + [AABB, HorizontalAdjacency, VerticalAdjacency]

    def _set_value(self, other, new_value):
        if not new_value:
            raise NotImplementedError("Inside does not support set_value(False)")

        state = og.sim.dump_state(serialized=False)

        for _ in range(10):
            if sample_kinematics("inside", self.obj, other) and self.get_value(other):
                return True
            else:
                og.sim.load_state(state, serialized=False)

        return False

    def _get_value(self, other):
        # First check that the inner object's position is inside the outer's AABB.
        # Since we usually check for a small set of outer objects, this is cheap.
        # Also note that this produces garbage values for fixed objects - but we are
        # assuming none of our inside-checking objects are fixed.
        aabb_lower, aabb_upper = self.obj.states[AABB].get_value()
        inner_object_pos = (aabb_lower + aabb_upper) / 2.0
        outer_object_aabb = other.states[AABB].get_value()

        if not BoundingBoxAPI.aabb_contains_point(inner_object_pos, outer_object_aabb):
            return False

        # Our definition of inside: an object A is inside an object B if there
        # exists a 3-D coordinate space in which object B can be found on both
        # sides of object A in at least 2 out of 3 of the coordinate axes. To
        # check this, we sample a bunch of coordinate systems (for the sake of
        # simplicity, all have their 3rd axes aligned with the Z axis but the
        # 1st and 2nd axes are free.
        vertical_adjacency = self.obj.states[VerticalAdjacency].get_value()
        horizontal_adjacency = self.obj.states[HorizontalAdjacency].get_value()

        # First, check if the body can be found on both sides in Z
        on_both_sides_Z = other in vertical_adjacency.negative_neighbors and other in vertical_adjacency.positive_neighbors
        if on_both_sides_Z:
            # If the object is on both sides of Z, we already found 1 axis, so just
            # find another axis where the object is on both sides.
            on_both_sides_in_any_axis = any(
                other in adjacency_list.positive_neighbors and
                other in adjacency_list.negative_neighbors
                for adjacency_list in flatten_planes(horizontal_adjacency)
            )
            return on_both_sides_in_any_axis

        # If the object was not on both sides of Z, then we need to look at each
        # plane and try to find one where the object is on both sides of both
        # axes in that plane.
        on_both_sides_of_both_axes_in_any_plane = any(
            other in adjacency_list_by_axis[0].positive_neighbors and
            other in adjacency_list_by_axis[0].negative_neighbors and
            other in adjacency_list_by_axis[1].positive_neighbors and
            other in adjacency_list_by_axis[1].negative_neighbors
            for adjacency_list_by_axis in horizontal_adjacency
        )
        return on_both_sides_of_both_axes_in_any_plane

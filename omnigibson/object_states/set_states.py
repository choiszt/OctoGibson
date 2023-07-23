from omnigibson.object_states.object_state_base import REGISTERED_OBJECT_STATES
from omnigibson.object_states.aabb import AABB
from omnigibson.object_states.adjacency import HorizontalAdjacency, VerticalAdjacency
from omnigibson.object_states.attached_to import AttachedTo
from omnigibson.object_states.burnt import Burnt
from omnigibson.object_states.contact_bodies import ContactBodies
from omnigibson.object_states.contact_particles import ContactParticles
from omnigibson.object_states.cooked import Cooked
from omnigibson.object_states.covered import Covered
from omnigibson.object_states.frozen import Frozen
from omnigibson.object_states.heat_source_or_sink import HeatSourceOrSink
from omnigibson.object_states.heated import Heated
from omnigibson.object_states.inside import Inside
from omnigibson.object_states.max_temperature import MaxTemperature
from omnigibson.object_states.next_to import NextTo
from omnigibson.object_states.on_fire import OnFire
from omnigibson.object_states.on_top import OnTop
from omnigibson.object_states.open import Open
from omnigibson.object_states.overlaid import Overlaid
from omnigibson.object_states.particle_modifier import ParticleRemover, ParticleApplier
from omnigibson.object_states.particle_source_or_sink import ParticleSource, ParticleSink
from omnigibson.object_states.pose import Pose
from omnigibson.object_states.saturated import Saturated
from omnigibson.object_states.sliced import Sliced
from omnigibson.object_states.slicer import Slicer
from omnigibson.object_states.temperature import Temperature
from omnigibson.object_states.toggle import ToggledOn
from omnigibson.object_states.touching import Touching
from omnigibson.object_states.under import Under
from omnigibson.object_states.filled import Filled
from omnigibson.object_states.folded import Folded
from omnigibson.object_states.unfolded import Unfolded
# don't have KinematicsMixin & ParticleModifier
def is_AttachedTo(obj):
    try:
        obj.states[AttachedTo].set_value(True) #TODO need more implement
    except:
        print(f"{obj}don't have states: AttachedTo")
        pass
def is_Burnt(obj,burnttemp):
    try:
        """
        set a new temp for burnt
        """
        obj.states[Burnt].set_value(burnttemp) 
    except:
        print(f"{obj}don't have states: Burnt")
        pass

def is_Cooked(obj,cooktemp):
    try:
        """
        set a new temp for cooked
        """
        obj.states[Cooked].set_value(cooktemp) 
    except:
        print(f"{obj}don't have states: Cooked")
        pass

def is_Covered(obj,cooktemp):
    try:
        """
        set a new temp for cooked
        """
        obj.states[Covered].set_value(cooktemp) 
    except:
        print(f"{obj}don't have states: Cooked")
        pass
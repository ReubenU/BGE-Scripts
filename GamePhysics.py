#   By Reuben Unicruz
#   License: MIT/BSD
#
#   This script is WIP

from bge import constraints

def createVehicle(GameObject):

    constraintType = constraints.VEHICLE_CONSTRAINT

    init_const = constraints.createConstraint(
        GameObject.getPhysicsId(),
        0,
        constraints.VEHICLE_CONSTRAINT
    )
    init_vehicle = init_const.getConstraintId()
    vehicle = constraints.getVehicleConstraint(init_vehicle)
    return vehicle

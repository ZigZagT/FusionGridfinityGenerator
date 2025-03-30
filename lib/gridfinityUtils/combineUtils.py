import math
import adsk.core, adsk.fusion, traceback
import os

from .const import DEFAULT_FILTER_TOLERANCE

from .geometryUtils import boundingBoxVolume


def cutBody(
    targetBody: adsk.fusion.BRepBodies,
    toolBodies: adsk.core.ObjectCollection,
    targetComponent: adsk.fusion.Component,
):
    combineInput = targetComponent.features.combineFeatures.createInput(
        targetBody, toolBodies
    )
    combineInput.operation = adsk.fusion.FeatureOperations.CutFeatureOperation
    combineFeature = targetComponent.features.combineFeatures.add(combineInput)
    return combineFeature


def intersectBody(
    targetBody: adsk.fusion.BRepBody,
    toolBodies: adsk.core.ObjectCollection,
    targetComponent: adsk.fusion.Component,
):
    combineInput = targetComponent.features.combineFeatures.createInput(
        targetBody, toolBodies
    )
    combineInput.operation = adsk.fusion.FeatureOperations.IntersectFeatureOperation
    combineFeature = targetComponent.features.combineFeatures.add(combineInput)
    return combineFeature


def joinBodies(
    targetBody: adsk.fusion.BRepBody,
    toolBodies: adsk.core.ObjectCollection,
    targetComponent: adsk.fusion.Component,
    keepToolBodies: bool = False,
) -> adsk.fusion.BRepBody:
    combineFeatures: adsk.fusion.CombineFeatures = (
        targetComponent.features.combineFeatures
    )
    combineFeatureInput = combineFeatures.createInput(targetBody, toolBodies)
    combineFeatureInput.operation = adsk.fusion.FeatureOperations.JoinFeatureOperation
    combineFeatureInput.isKeepToolBodies = keepToolBodies
    combineFeature = combineFeatures.add(combineFeatureInput)
    return combineFeature.bodies.item(0)

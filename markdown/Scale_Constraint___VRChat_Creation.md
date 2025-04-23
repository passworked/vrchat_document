[Skip to main content](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-scale-constraint/#__docusaurus_skipToContent_fallback)

On this page

The `VRCScaleConstraint` component changes the scale of the target transform to match the scales of its sources.

![](https://creators.vrchat.com/assets/images/scale-db75226ea9a6b46306b511bb70d5f1f5.png)

*   **Is Active** - Controls whether the constraint will be evaluated or not. Disabling the entire component and deactivating the game object with the component on it will also stop the constraint from running.
*   **Weight** - Controls the overall weight applied to this constraint.
    *   This should normally be in the range 0 to 1, but you can tick the `Free edit` box if you want to set values outside of that range.

The two buttons at the top the inspector are utilities to let you:

*   **Activate** the constraint. This saves the current offset from the sources, then activates and locks the constraint.
*   **Zero out** the constraint. This resets the offset to its default value, then activates and locks the constraint.

Constraint Settings[​](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-scale-constraint/#constraint-settings "Direct link to Constraint Settings")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   **Scale At Rest** - Defines the transform's scale when the constraint's overall weight is 0.
*   **Scale Offset** - Defines the offset applied to the result of this constraint.
*   **Lock** - When enabled, locks the `At Rest` and `Offset` values in place, preventing them from being edited.
    *   If you activate the constraint and leave these values unlocked, they'll be recalculated as the target transform's scale changes.
    *   If you lock these values and activate the constraint, the constraint will start taking control of the transform.
*   **Freeze Scale Axes** - Allows you to exclude specific axes from evaluation as the constraint is solved. By default, all three axes are selected for evaluation.

Sources[​](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-scale-constraint/#sources "Direct link to Sources")

-----------------------------------------------------------------------------------------------------------------------------------

The "Sources" list determines which transforms affect this constraint. Click the `+` button in the bottom right to add a new source. Click the `-` button to remove the currently selected source. Each source has the following options:

*   **Source Transform** - The transform to use as a source.
*   **Weight** - Controls how much this source should affect the constraint.
    *   This should normally be in the range 0 to 1, but you can tick the `Free edit` box if you want to set values outside of that range.

Advanced[​](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-scale-constraint/#advanced "Direct link to Advanced")

--------------------------------------------------------------------------------------------------------------------------------------

*   **Target Transform** - Defines the transform affected by this constraint component. If left empty, the transform this constraint is attached to will be affected instead.
*   **Solve In Local Space** - If ticked, this constraint will be solved as if the sources are in local space rather than world space.
*   **Freeze To World** - If ticked, this constraint will ignore its sources and keep a fixed scale instead.
*   **Rebake Offsets When Unfrozen** - If ticked, this constraint will rebake its offsets relative to its sources when `Freeze To World` is disabled.

See the parent section covering [Advanced Constraint Settings](https://creators.vrchat.com/avatars/avatar-dynamics/constraints#advanced-constraint-settings)
 for a more in-depth description of how these advanced settings work.

*   [Constraint Settings](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-scale-constraint/#constraint-settings)
    
*   [Sources](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-scale-constraint/#sources)
    
*   [Advanced](https://creators.vrchat.com/avatars/avatar-dynamics/constraints/vrc-scale-constraint/#advanced)
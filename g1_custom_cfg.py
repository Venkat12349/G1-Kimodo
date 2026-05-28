from robojudo.config import cfg_registry
from robojudo.controller.ctrl_cfgs import (
    JoystickCtrlCfg,  # noqa: F401
    KeyboardCtrlCfg,  # noqa: F401
    UnitreeCtrlCfg,  # noqa: F401
)
from robojudo.pipeline.pipeline_cfgs import (
    RlLocoMimicPipelineCfg,  # noqa: F401
    RlMultiPolicyPipelineCfg,  # noqa: F401
    RlPipelineCfg,  # noqa: F401
)

from .ctrl.g1_beyondmimic_ctrl_cfg import G1BeyondmimicCtrlCfg  # noqa: F401
from .ctrl.g1_motion_ctrl_cfg import (  # noqa: F401
    G1MotionCtrlCfg,
    G1MotionH2HCtrlCfg,
    G1MotionKungfuBotCtrlCfg,
    G1MotionTwistCtrlCfg,
)
from .ctrl.g1_twist_redis_ctrl_cfg import G1TwistRedisCtrlCfg  # noqa: F401
from .env.g1_dummy_env_cfg import G1DummyEnvCfg  # noqa: F401
from .env.g1_mujuco_env_cfg import (
    G1_12MujocoEnvCfg,
    G1_23MujocoEnvCfg,
    G1MujocoEnvCfg,
)  # noqa: F401
from .env.g1_real_env_cfg import G1RealEnvCfg, G1UnitreeCfg  # noqa: F401
from .policy.g1_amo_policy_cfg import G1AmoPolicyCfg  # noqa: F401
from .policy.g1_asap_policy_cfg import (
    G1AsapLocoPolicyCfg,
    G1AsapPolicyCfg,
)  # noqa: F401
from .policy.g1_beyondmimic_policy_cfg import G1BeyondMimicPolicyCfg  # noqa: F401
from .policy.g1_h2h_policy_cfg import G1H2HPolicyCfg  # noqa: F401
from .policy.g1_kungfubot_policy_cfg import (
    G1KungfuBotGeneralPolicyCfg,
    G1KungfuBotPolicyCfg,
)  # noqa: F401
from .policy.g1_smooth_policy_cfg import G1SmoothPolicyCfg  # noqa: F401
from .policy.g1_twist_policy_cfg import G1TwistPolicyCfg  # noqa: F401
from .policy.g1_unitree_policy_cfg import (
    G1UnitreePolicyCfg,
    G1UnitreeWoGaitPolicyCfg,
)  # noqa: F401

# ======================== Custom Configs ======================== #
"""
Add your custom config here.
"""
from .g1_cfg import g1_protomotions_tracker

from .policy.g1_protomotions_tracker_cfg import (
    ProtoMotionsTrackerPolicyCfg,
)  # noqa: F401


@cfg_registry.register
class g1_protomotions_bm_tracker(RlPipelineCfg):
    """ProtoMotions BM tracker — sim, hardcoded paths."""

    device: str = "auto"
    # run_fullspeed: bool = True
    robot: str = "g1"
    env: G1MujocoEnvCfg = G1MujocoEnvCfg(
        born_place_align=False,
        random_heading=True,
    )
    ctrl: list[KeyboardCtrlCfg] = [
        KeyboardCtrlCfg(
            triggers={
                "r": "[MOTION_RESET]",
                "i": "[SIM_REBORN]",
                "o": "[SHUTDOWN]",
                "<": "[MOTION_FADE_IN]",
                ">": "[MOTION_FADE_OUT]",
            },
        ),
    ]
    policy: ProtoMotionsTrackerPolicyCfg = ProtoMotionsTrackerPolicyCfg(
        onnx_path="/home/aiemumbai-devise/Projects/humanoid/packages/ProtoMotions/data/pretrained_models/motion_tracker/g1-bones-deploy/compiled_models/unified_pipeline.onnx",
        motion_path="/home/aiemumbai-devise/Projects/humanoid/packages/ProtoMotions/data/g1-kimodo-generated/proto/output_wave.motion",
    )


@cfg_registry.register
class g1_protomotions_bm_tracker_real(RlPipelineCfg):
    robot: str = "g1"
    env: G1RealEnvCfg = G1RealEnvCfg(
        env_type="UnitreeCppEnv",
        unitree=G1UnitreeCfg(net_if="eno2"),
        born_place_align=False,
    )
    ctrl: list = [
        UnitreeCtrlCfg(),
        KeyboardCtrlCfg(
            triggers={
                "r": "[MOTION_RESET]",
                "i": "[SIM_REBORN]",
                "o": "[SHUTDOWN]",
                "<": "[MOTION_FADE_IN]",
                ">": "[MOTION_FADE_OUT]",
            },
        ),
    ]
    do_safety_check: bool = True
    policy: ProtoMotionsTrackerPolicyCfg = ProtoMotionsTrackerPolicyCfg(
        onnx_path="/home/aiemumbai-devise/Projects/humanoid/packages/ProtoMotions/data/pretrained_models/motion_tracker/g1-bones-deploy/compiled_models/unified_pipeline.onnx",
        motion_path="/home/aiemumbai-devise/Projects/humanoid/packages/ProtoMotions/data/g1-kimodo-generated/proto/output_wave.motion",
    )


@cfg_registry.register
class g1_dev(RlPipelineCfg):
    robot: str = "g1"
    env: G1_23MujocoEnvCfg = G1_23MujocoEnvCfg()

    ctrl: list[KeyboardCtrlCfg] = [
        KeyboardCtrlCfg(),
    ]

    policy: G1UnitreePolicyCfg = G1UnitreePolicyCfg()

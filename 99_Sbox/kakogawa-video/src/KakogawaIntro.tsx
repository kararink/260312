import {
    AbsoluteFill,
    useCurrentFrame,
    useVideoConfig,
    Sequence,
    interpolate,
} from "remotion";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import { slide } from "@remotion/transitions/slide";
import { fade } from "@remotion/transitions/fade";
import { Scene1Opening } from "./scenes/Scene1Opening";
import { Scene2Roads } from "./scenes/Scene2Roads";
import { Scene3Disaster } from "./scenes/Scene3Disaster";
import { Scene4Community } from "./scenes/Scene4Community";
import { Scene5Closing } from "./scenes/Scene5Closing";

export const KakogawaIntro: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    return (
        <AbsoluteFill style={{ backgroundColor: "#0a0e27" }}>
            <TransitionSeries>
                {/* Scene 1: オープニング (0〜3.5s = 105フレーム) */}
                <TransitionSeries.Sequence durationInFrames={Math.round(3.5 * fps)}>
                    <Scene1Opening />
                </TransitionSeries.Sequence>

                <TransitionSeries.Transition
                    presentation={slide({ direction: "from-right" })}
                    timing={linearTiming({ durationInFrames: 15 })}
                />

                {/* Scene 2: 道路・橋梁 (3s = 90フレーム) */}
                <TransitionSeries.Sequence durationInFrames={Math.round(3 * fps)}>
                    <Scene2Roads />
                </TransitionSeries.Sequence>

                <TransitionSeries.Transition
                    presentation={fade()}
                    timing={linearTiming({ durationInFrames: 15 })}
                />

                {/* Scene 3: 河川・防災 (3s = 90フレーム) */}
                <TransitionSeries.Sequence durationInFrames={Math.round(3 * fps)}>
                    <Scene3Disaster />
                </TransitionSeries.Sequence>

                <TransitionSeries.Transition
                    presentation={slide({ direction: "from-bottom" })}
                    timing={linearTiming({ durationInFrames: 15 })}
                />

                {/* Scene 4: 地域連携 (3s = 90フレーム) */}
                <TransitionSeries.Sequence durationInFrames={Math.round(3 * fps)}>
                    <Scene4Community />
                </TransitionSeries.Sequence>

                <TransitionSeries.Transition
                    presentation={fade()}
                    timing={linearTiming({ durationInFrames: 20 })}
                />

                {/* Scene 5: クロージング (3s = 90フレーム) */}
                <TransitionSeries.Sequence durationInFrames={Math.round(3 * fps)}>
                    <Scene5Closing />
                </TransitionSeries.Sequence>
            </TransitionSeries>
        </AbsoluteFill>
    );
};

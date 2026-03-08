import {
    AbsoluteFill,
    useCurrentFrame,
    useVideoConfig,
    interpolate,
    spring,
} from "remotion";
import { loadFont } from "@remotion/google-fonts/NotoSansJP";

const { fontFamily } = loadFont("normal", {
    weights: ["400", "700", "900"],
    subsets: ["latin"],
});

export const Scene5Closing: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // ── メインCTA ──
    const mainSpring = spring({
        frame,
        fps,
        config: { damping: 10, stiffness: 80 },
    });

    // ── サブ ──
    const subSpring = spring({
        frame,
        fps,
        delay: 15,
        config: { damping: 200 },
    });

    // ── CTA ボタン ──
    const ctaSpring = spring({
        frame,
        fps,
        delay: 25,
        config: { damping: 12, stiffness: 150 },
    });

    // ── 光のリング ──
    const ringScale = interpolate(frame, [0, 2.5 * fps], [0.2, 2], {
        extrapolateRight: "clamp",
    });
    const ringOpacity = interpolate(
        frame,
        [0, 0.5 * fps, 2.5 * fps],
        [0, 0.15, 0],
        { extrapolateRight: "clamp" }
    );

    // ── パルス ──
    const pulse = Math.sin(frame * 0.06) * 0.015 + 1;

    // ── 装飾ドット ──
    const dots = Array.from({ length: 12 }, (_, i) => {
        const angle = (i / 12) * Math.PI * 2;
        const radius = 320;
        const dotSpring = spring({
            frame,
            fps,
            delay: 8 + i * 3,
            config: { damping: 15, stiffness: 150 },
        });
        const x = 960 + Math.cos(angle) * radius * dotSpring;
        const y = 540 + Math.sin(angle) * radius * dotSpring;
        return { x, y, opacity: dotSpring, key: i };
    });

    return (
        <AbsoluteFill
            style={{
                background:
                    "radial-gradient(ellipse at center, #0a2540 0%, #051525 50%, #020b14 100%)",
                fontFamily,
                overflow: "hidden",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
            }}
        >
            {/* 光のリング */}
            <div
                style={{
                    position: "absolute",
                    left: "50%",
                    top: "50%",
                    width: 700,
                    height: 700,
                    borderRadius: "50%",
                    border: "2px solid rgba(92,168,232,0.3)",
                    transform: `translate(-50%, -50%) scale(${ringScale})`,
                    opacity: ringOpacity,
                }}
            />

            {/* 装飾ドット */}
            {dots.map((d) => (
                <div
                    key={d.key}
                    style={{
                        position: "absolute",
                        left: d.x - 5,
                        top: d.y - 5,
                        width: 10,
                        height: 10,
                        borderRadius: "50%",
                        backgroundColor: "#5ca8e8",
                        opacity: d.opacity * 0.4,
                        boxShadow: "0 0 12px rgba(92,168,232,0.5)",
                    }}
                />
            ))}

            {/* メインコンテンツ */}
            <div
                style={{
                    textAlign: "center",
                    transform: `scale(${pulse})`,
                }}
            >
                {/* メインCTA */}
                <div
                    style={{
                        fontSize: 96,
                        fontWeight: 900,
                        color: "#ffffff",
                        letterSpacing: 10,
                        textShadow:
                            "0 0 60px rgba(92,168,232,0.5), 0 4px 20px rgba(0,0,0,0.5)",
                        marginBottom: 20,
                        transform: `scale(${interpolate(mainSpring, [0, 1], [1.2, 1])})`,
                        opacity: mainSpring,
                    }}
                >
                    あなたの力が、必要だ。
                </div>

                {/* 装飾ライン */}
                <div
                    style={{
                        width: interpolate(subSpring, [0, 1], [0, 500]),
                        height: 3,
                        background:
                            "linear-gradient(90deg, transparent, #ff9800 30%, #ffb74d 50%, #ff9800 70%, transparent)",
                        margin: "0 auto 30px",
                    }}
                />

                {/* 事務所名 */}
                <div
                    style={{
                        fontSize: 36,
                        fontWeight: 900,
                        color: "#a0d4ff",
                        letterSpacing: 10,
                        opacity: subSpring,
                        transform: `translateY(${interpolate(subSpring, [0, 1], [20, 0])}px)`,
                        marginBottom: 50,
                    }}
                >
                    兵庫県 加古川土木事務所
                </div>

                {/* CTAボタン */}
                <div
                    style={{
                        display: "inline-block",
                        transform: `scale(${interpolate(ctaSpring, [0, 1], [0.8, 1])})`,
                        opacity: ctaSpring,
                    }}
                >
                    <div
                        style={{
                            fontSize: 32,
                            fontWeight: 900,
                            color: "#ffffff",
                            letterSpacing: 6,
                            border: "3px solid #ff9800",
                            borderRadius: 16,
                            padding: "18px 60px",
                            background:
                                "linear-gradient(135deg, rgba(255,152,0,0.15), rgba(255,152,0,0.05))",
                            boxShadow: "0 0 30px rgba(255,152,0,0.2)",
                        }}
                    >
                        土木職 採用情報はこちら
                    </div>
                </div>

                {/* 所在地 */}
                <div
                    style={{
                        marginTop: 40,
                        fontSize: 18,
                        color: "#546e7a",
                        letterSpacing: 3,
                        fontWeight: 400,
                        opacity: interpolate(ctaSpring, [0, 1], [0, 0.7]),
                    }}
                >
                    〒675-8566 加古川市加古川町寺家町天神木97-1 加古川総合庁舎
                </div>
            </div>
        </AbsoluteFill>
    );
};

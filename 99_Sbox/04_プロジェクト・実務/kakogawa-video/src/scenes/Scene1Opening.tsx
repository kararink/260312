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

export const Scene1Opening: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // ── 背景グラデーションシフト ──
    const bgShift = interpolate(frame, [0, 3 * fps], [0, 40], {
        extrapolateRight: "clamp",
    });

    // ── メインキャッチ（巨大文字）──
    const mainSpring = spring({
        frame,
        fps,
        config: { damping: 10, stiffness: 80 },
    });
    const mainScale = interpolate(mainSpring, [0, 1], [1.3, 1]);
    const mainOpacity = interpolate(mainSpring, [0, 1], [0, 1]);

    // ── サブキャッチ ──
    const subSpring = spring({
        frame,
        fps,
        delay: 20,
        config: { damping: 200 },
    });

    // ── 兵庫県バッジ ──
    const badgeSpring = spring({
        frame,
        fps,
        delay: 8,
        config: { damping: 12, stiffness: 150 },
    });

    // ── 装飾ライン ──
    const lineProgress = interpolate(frame, [0.3 * fps, 1.5 * fps], [0, 100], {
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp",
    });

    // ── パーティクル ──
    const particles = Array.from({ length: 30 }, (_, i) => {
        const angle = (i / 30) * Math.PI * 2;
        const radius = 350 + Math.sin(i * 1.5) * 120;
        const speed = 0.4 + (i % 4) * 0.2;
        const x = 960 + Math.cos(angle + frame * 0.012 * speed) * radius;
        const y = 540 + Math.sin(angle + frame * 0.012 * speed) * radius;
        const size = 2 + (i % 5) * 2;
        const opacity = interpolate(
            frame,
            [0, 0.8 * fps],
            [0, 0.15 + (i % 4) * 0.1],
            { extrapolateRight: "clamp" }
        );
        return { x, y, size, opacity, key: i };
    });

    return (
        <AbsoluteFill
            style={{
                background: `linear-gradient(${130 + bgShift}deg, #020b1a 0%, #0a2540 35%, #1a4470 65%, #0a2540 100%)`,
                fontFamily,
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                overflow: "hidden",
            }}
        >
            {/* パーティクル */}
            {particles.map((p) => (
                <div
                    key={p.key}
                    style={{
                        position: "absolute",
                        left: p.x,
                        top: p.y,
                        width: p.size,
                        height: p.size,
                        borderRadius: "50%",
                        backgroundColor: "#5ca8e8",
                        opacity: p.opacity,
                        boxShadow: "0 0 6px rgba(92,168,232,0.3)",
                    }}
                />
            ))}

            {/* 兵庫県バッジ */}
            <div
                style={{
                    position: "absolute",
                    top: 200,
                    left: "50%",
                    transform: `translate(-50%, 0) scale(${badgeSpring})`,
                    opacity: badgeSpring,
                    background: "rgba(92,168,232,0.12)",
                    border: "2px solid rgba(92,168,232,0.4)",
                    borderRadius: 12,
                    padding: "12px 50px",
                    fontSize: 36,
                    fontWeight: 900,
                    color: "#7ec8f0",
                    letterSpacing: 16,
                }}
            >
                兵庫県
            </div>

            {/* 装飾ライン上 */}
            <div
                style={{
                    position: "absolute",
                    top: 310,
                    left: "50%",
                    transform: "translateX(-50%)",
                    width: `${lineProgress * 0.7}%`,
                    maxWidth: 800,
                    height: 3,
                    background:
                        "linear-gradient(90deg, transparent, #5ca8e8 30%, #a0d4ff 50%, #5ca8e8 70%, transparent)",
                }}
            />

            {/* メインタイトル */}
            <div
                style={{
                    position: "absolute",
                    top: "50%",
                    left: "50%",
                    transform: `translate(-50%, -50%) scale(${mainScale})`,
                    opacity: mainOpacity,
                    textAlign: "center",
                    whiteSpace: "nowrap",
                }}
            >
                <div
                    style={{
                        fontSize: 110,
                        fontWeight: 900,
                        color: "#ffffff",
                        letterSpacing: 12,
                        textShadow:
                            "0 4px 40px rgba(92,168,232,0.5), 0 0 80px rgba(92,168,232,0.2)",
                        lineHeight: 1.2,
                    }}
                >
                    加古川土木事務所
                </div>
            </div>

            {/* サブキャッチ */}
            <div
                style={{
                    position: "absolute",
                    top: 640,
                    left: "50%",
                    transform: `translate(-50%, 0) translateY(${interpolate(subSpring, [0, 1], [30, 0])}px)`,
                    opacity: subSpring,
                    textAlign: "center",
                }}
            >
                <div
                    style={{
                        fontSize: 38,
                        fontWeight: 700,
                        color: "#a0d4ff",
                        letterSpacing: 10,
                    }}
                >
                    この街の未来を、つくる仕事。
                </div>
            </div>

            {/* 装飾ライン下 */}
            <div
                style={{
                    position: "absolute",
                    top: 720,
                    left: "50%",
                    transform: "translateX(-50%)",
                    width: `${lineProgress * 0.5}%`,
                    maxWidth: 500,
                    height: 2,
                    background:
                        "linear-gradient(90deg, transparent, #5ca8e8, transparent)",
                }}
            />

            {/* RECRUIT バッジ */}
            <div
                style={{
                    position: "absolute",
                    bottom: 140,
                    left: "50%",
                    transform: `translate(-50%, 0) scale(${subSpring})`,
                    opacity: subSpring * 0.8,
                    fontSize: 22,
                    fontWeight: 700,
                    color: "#ff9800",
                    letterSpacing: 8,
                    border: "2px solid rgba(255,152,0,0.4)",
                    borderRadius: 8,
                    padding: "8px 40px",
                    background: "rgba(255,152,0,0.08)",
                }}
            >
                RECRUIT 2026
            </div>
        </AbsoluteFill>
    );
};

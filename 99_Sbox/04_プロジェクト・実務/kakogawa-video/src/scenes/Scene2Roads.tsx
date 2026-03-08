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

// ── マンガ風ミニアイコン：街並み ──
const MangaCity: React.FC<{ progress: number; color: string }> = ({ progress, color }) => (
    <svg width={70} height={70} viewBox="0 0 70 70">
        <rect x={10} y={20} width={14} height={35} rx={2} fill="none" stroke={color} strokeWidth={2.5}
            strokeDasharray={100} strokeDashoffset={100 * (1 - progress)} />
        <rect x={28} y={10} width={14} height={45} rx={2} fill="none" stroke={color} strokeWidth={2.5}
            strokeDasharray={120} strokeDashoffset={120 * (1 - progress)} />
        <rect x={46} y={25} width={14} height={30} rx={2} fill="none" stroke={color} strokeWidth={2.5}
            strokeDasharray={90} strokeDashoffset={90 * (1 - progress)} />
        {/* 窓 */}
        {[[15, 28], [15, 38], [33, 18], [33, 28], [33, 38], [51, 33], [51, 43]].map(([x, y], i) => (
            <rect key={i} x={x} y={y} width={4} height={4} fill={color} opacity={progress * 0.6} rx={0.5} />
        ))}
        {/* 地面 */}
        <line x1={5} y1={55} x2={65} y2={55} stroke={color} strokeWidth={2} opacity={progress * 0.4} />
    </svg>
);

// ── マンガ風ミニアイコン：波（河川） ──
const MangaWaves: React.FC<{ progress: number; color: string }> = ({ progress, color }) => (
    <svg width={70} height={70} viewBox="0 0 70 70">
        <path d="M5 25 Q17 15 28 25 Q40 35 52 25 Q58 20 65 25" fill="none" stroke={color} strokeWidth={3}
            strokeLinecap="round" strokeDasharray={100} strokeDashoffset={100 * (1 - progress)} />
        <path d="M5 38 Q17 28 28 38 Q40 48 52 38 Q58 33 65 38" fill="none" stroke={color} strokeWidth={2.5}
            strokeLinecap="round" opacity={progress * 0.7} />
        <path d="M5 50 Q17 40 28 50 Q40 60 52 50 Q58 45 65 50" fill="none" stroke={color} strokeWidth={2}
            strokeLinecap="round" opacity={progress * 0.4} />
        {/* 水飛沫 */}
        <circle cx={20} cy={18} r={2} fill={color} opacity={progress * 0.4} />
        <circle cx={45} cy={20} r={1.5} fill={color} opacity={progress * 0.3} />
    </svg>
);

// ── マンガ風ミニアイコン：盾（防災） ──
const MangaShield: React.FC<{ progress: number; color: string }> = ({ progress, color }) => (
    <svg width={70} height={70} viewBox="0 0 70 70">
        <path d="M35 5 L60 18 L60 40 C60 52 48 62 35 68 C22 62 10 52 10 40 L10 18 Z"
            fill="none" stroke={color} strokeWidth={3}
            strokeDasharray={180} strokeDashoffset={180 * (1 - progress)} strokeLinejoin="round" />
        {/* チェックマーク */}
        <path d="M22 36 L32 46 L50 25" fill="none" stroke={color} strokeWidth={3.5}
            strokeLinecap="round" strokeLinejoin="round" opacity={progress} />
    </svg>
);

// ── マンガ風ミニアイコン：書類（許認可） ──
const MangaDocument: React.FC<{ progress: number; color: string }> = ({ progress, color }) => (
    <svg width={70} height={70} viewBox="0 0 70 70">
        {/* 書類 */}
        <rect x={12} y={5} width={38} height={50} rx={3} fill="none" stroke={color} strokeWidth={2.5}
            strokeDasharray={180} strokeDashoffset={180 * (1 - progress)} />
        {/* 折り返し */}
        <path d="M50 5 L50 18 L38 18" fill="none" stroke={color} strokeWidth={2} opacity={progress * 0.6} />
        {/* テキスト行 */}
        {[22, 30, 38, 46].map((y, i) => (
            <line key={i} x1={20} y1={y} x2={20 + (i < 3 ? 22 : 14)} y2={y}
                stroke={color} strokeWidth={2} strokeLinecap="round" opacity={progress * 0.5} />
        ))}
        {/* 判子 */}
        <circle cx={42} cy={42} r={8} fill="none" stroke="#ff5252" strokeWidth={2} opacity={progress} />
        <text x={42} y={46} textAnchor="middle" fontSize={7} fontWeight={900} fill="#ff5252" opacity={progress}>許可</text>
    </svg>
);

// アニメーション付きメトリックカード
const MetricCard: React.FC<{
    icon: React.ReactNode;
    value: string;
    label: string;
    delay: number;
    accentColor: string;
}> = ({ icon, value, label, delay, accentColor }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const s = spring({
        frame,
        fps,
        delay,
        config: { damping: 12, stiffness: 150 },
    });

    return (
        <div
            style={{
                width: 260,
                background: "rgba(255,255,255,0.04)",
                border: `2px solid ${accentColor}30`,
                borderRadius: 20,
                padding: "30px 20px",
                textAlign: "center",
                transform: `scale(${interpolate(s, [0, 1], [0.7, 1])}) translateY(${interpolate(s, [0, 1], [50, 0])}px)`,
                opacity: s,
            }}
        >
            <div style={{ display: "flex", justifyContent: "center", marginBottom: 8 }}>{icon}</div>
            <div
                style={{
                    fontSize: 48,
                    fontWeight: 900,
                    color: accentColor,
                    letterSpacing: 2,
                }}
            >
                {value}
            </div>
            <div
                style={{
                    fontSize: 20,
                    fontWeight: 700,
                    color: "#b0bec5",
                    letterSpacing: 3,
                    marginTop: 6,
                }}
            >
                {label}
            </div>
        </div>
    );
};

export const Scene2Roads: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const titleSpring = spring({
        frame,
        fps,
        config: { damping: 12, stiffness: 100 },
    });

    const lineWidth = interpolate(frame, [0, 1.5 * fps], [0, 100], {
        extrapolateRight: "clamp",
    });

    const iconProgress = interpolate(frame, [0, 1.2 * fps], [0, 1], {
        extrapolateRight: "clamp",
    });

    return (
        <AbsoluteFill
            style={{
                background:
                    "linear-gradient(160deg, #020b1a 0%, #0d2240 50%, #020b1a 100%)",
                fontFamily,
                overflow: "hidden",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                gap: 50,
            }}
        >
            {/* 背景グリッド */}
            <div
                style={{
                    position: "absolute",
                    inset: 0,
                    backgroundImage:
                        "linear-gradient(rgba(92,168,232,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(92,168,232,0.04) 1px, transparent 1px)",
                    backgroundSize: "80px 80px",
                }}
            />

            {/* 装飾ライン */}
            <div
                style={{
                    position: "absolute",
                    top: 180,
                    left: "50%",
                    transform: "translateX(-50%)",
                    width: `${lineWidth * 0.6}%`,
                    maxWidth: 600,
                    height: 2,
                    background:
                        "linear-gradient(90deg, transparent, #5ca8e8, transparent)",
                }}
            />

            {/* メインキャッチ */}
            <div
                style={{
                    textAlign: "center",
                    transform: `scale(${interpolate(titleSpring, [0, 1], [0.8, 1])})`,
                    opacity: titleSpring,
                }}
            >
                <div
                    style={{
                        fontSize: 80,
                        fontWeight: 900,
                        color: "#ffffff",
                        letterSpacing: 6,
                        textShadow: "0 4px 30px rgba(92,168,232,0.4)",
                        marginBottom: 16,
                    }}
                >
                    地域を支えるスケール
                </div>
                <div
                    style={{
                        fontSize: 30,
                        fontWeight: 700,
                        color: "#7ec8f0",
                        letterSpacing: 6,
                    }}
                >
                    道路・河川・港湾 ─ 5市町の社会基盤を守る
                </div>
            </div>

            {/* メトリックカード */}
            <div
                style={{
                    display: "flex",
                    gap: 40,
                    justifyContent: "center",
                }}
            >
                <MetricCard
                    icon={<MangaCity progress={iconProgress} color="#ffd54f" />}
                    value="5市町"
                    label="加古川・明石・高砂 他"
                    delay={Math.round(0.5 * fps)}
                    accentColor="#ffd54f"
                />
                <MetricCard
                    icon={<MangaWaves progress={iconProgress} color="#4fc3f7" />}
                    value="23河川"
                    label="一級10 ＋ 二級13"
                    delay={Math.round(0.7 * fps)}
                    accentColor="#4fc3f7"
                />
                <MetricCard
                    icon={<MangaShield progress={iconProgress} color="#81c784" />}
                    value="総合治水"
                    label="流域圏の防災"
                    delay={Math.round(0.9 * fps)}
                    accentColor="#81c784"
                />
                <MetricCard
                    icon={<MangaDocument progress={iconProgress} color="#ff8a65" />}
                    value="許可"
                    label="建設業・宅建業 等"
                    delay={Math.round(1.1 * fps)}
                    accentColor="#ff8a65"
                />
            </div>
        </AbsoluteFill>
    );
};

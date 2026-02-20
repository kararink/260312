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

// ── SVGアイコン：シールド＋波（街を守る）──
const ShieldWaveIcon: React.FC<{ progress: number }> = ({ progress }) => (
    <svg width={100} height={100} viewBox="0 0 100 100">
        {/* シールド */}
        <path
            d="M50 8 L85 25 L85 55 C85 72 68 88 50 95 C32 88 15 72 15 55 L15 25 Z"
            fill="none"
            stroke="#4fc3f7"
            strokeWidth={3}
            strokeDasharray={280}
            strokeDashoffset={280 * (1 - progress)}
            strokeLinejoin="round"
        />
        {/* 波 */}
        <path
            d="M30 50 Q40 38 50 50 Q60 62 70 50"
            fill="none"
            stroke="#4fc3f7"
            strokeWidth={3}
            strokeLinecap="round"
            opacity={progress}
        />
        <path
            d="M30 62 Q40 50 50 62 Q60 74 70 62"
            fill="none"
            stroke="#4fc3f7"
            strokeWidth={2}
            strokeLinecap="round"
            opacity={progress * 0.6}
        />
    </svg>
);

// ── SVGアイコン：橋（地図に残る仕事）──
const BridgeLandmarkIcon: React.FC<{ progress: number }> = ({ progress }) => (
    <svg width={100} height={100} viewBox="0 0 100 100">
        {/* 橋のアーチ */}
        <path
            d="M10 65 Q30 30 50 65 Q70 30 90 65"
            fill="none"
            stroke="#81c784"
            strokeWidth={3.5}
            strokeDasharray={180}
            strokeDashoffset={180 * (1 - progress)}
            strokeLinecap="round"
        />
        {/* 橋脚 */}
        <line x1={30} y1={48} x2={30} y2={80} stroke="#81c784" strokeWidth={2.5} opacity={progress} />
        <line x1={50} y1={65} x2={50} y2={80} stroke="#81c784" strokeWidth={2.5} opacity={progress} />
        <line x1={70} y1={48} x2={70} y2={80} stroke="#81c784" strokeWidth={2.5} opacity={progress} />
        {/* 道路面 */}
        <line x1={10} y1={65} x2={90} y2={65} stroke="#81c784" strokeWidth={2} opacity={progress * 0.5} />
        {/* ロケーションピン */}
        <circle cx={50} cy={22} r={8} fill="none" stroke="#81c784" strokeWidth={2} opacity={progress} />
        <circle cx={50} cy={22} r={3} fill="#81c784" opacity={progress} />
        <path d="M50 30 L50 38" stroke="#81c784" strokeWidth={2} opacity={progress} />
    </svg>
);

// ── SVGアイコン：人と歯車（地域と成長）──
const CommunityGrowIcon: React.FC<{ progress: number }> = ({ progress }) => (
    <svg width={100} height={100} viewBox="0 0 100 100">
        {/* 中央の人 */}
        <circle cx={50} cy={30} r={10} fill="none" stroke="#ffb74d" strokeWidth={2.5} opacity={progress} />
        <path d="M35 55 Q35 42 50 42 Q65 42 65 55" fill="none" stroke="#ffb74d" strokeWidth={2.5} strokeLinecap="round"
            strokeDasharray={80} strokeDashoffset={80 * (1 - progress)} />
        {/* 左の人 */}
        <circle cx={22} cy={45} r={7} fill="none" stroke="#ffb74d" strokeWidth={2} opacity={progress * 0.7} />
        <path d="M12 65 Q12 55 22 55 Q32 55 32 65" fill="none" stroke="#ffb74d" strokeWidth={2} strokeLinecap="round" opacity={progress * 0.7} />
        {/* 右の人 */}
        <circle cx={78} cy={45} r={7} fill="none" stroke="#ffb74d" strokeWidth={2} opacity={progress * 0.7} />
        <path d="M68 65 Q68 55 78 55 Q88 55 88 65" fill="none" stroke="#ffb74d" strokeWidth={2} strokeLinecap="round" opacity={progress * 0.7} />
        {/* つながりの線 */}
        <line x1={32} y1={50} x2={40} y2={45} stroke="#ffb74d" strokeWidth={1.5} opacity={progress * 0.5} strokeDasharray="4 3" />
        <line x1={68} y1={50} x2={60} y2={45} stroke="#ffb74d" strokeWidth={1.5} opacity={progress * 0.5} strokeDasharray="4 3" />
        {/* 上昇矢印 */}
        <path d="M50 75 L50 85 M46 81 L50 85 L54 81" stroke="#ffb74d" strokeWidth={2} strokeLinecap="round" opacity={progress} />
    </svg>
);

// 仕事の魅力カード
const AppealCard: React.FC<{
    icon: React.ReactNode;
    title: string;
    desc: string;
    delay: number;
    accentColor: string;
}> = ({ icon, title, desc, delay, accentColor }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const s = spring({
        frame,
        fps,
        delay,
        config: { damping: 12, stiffness: 120 },
    });

    return (
        <div
            style={{
                display: "flex",
                alignItems: "center",
                gap: 30,
                transform: `translateX(${interpolate(s, [0, 1], [100, 0])}px)`,
                opacity: s,
                background: "rgba(255,255,255,0.03)",
                border: `1px solid ${accentColor}25`,
                borderRadius: 20,
                padding: "24px 40px 24px 30px",
            }}
        >
            {/* SVGアイコン */}
            <div
                style={{
                    minWidth: 110,
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    background: `${accentColor}10`,
                    borderRadius: 16,
                    padding: 10,
                }}
            >
                {icon}
            </div>

            <div>
                <div
                    style={{
                        fontSize: 44,
                        fontWeight: 900,
                        color: "#ffffff",
                        letterSpacing: 4,
                        marginBottom: 6,
                    }}
                >
                    {title}
                </div>
                <div
                    style={{
                        fontSize: 24,
                        fontWeight: 400,
                        color: "#90a4ae",
                        letterSpacing: 2,
                    }}
                >
                    {desc}
                </div>
            </div>
        </div>
    );
};

export const Scene3Disaster: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    // ── ヘッダー ──
    const headerSpring = spring({
        frame,
        fps,
        config: { damping: 15, stiffness: 100 },
    });

    // ── アイコンの進捗 ──
    const iconProgress = interpolate(frame, [0, 1.5 * fps], [0, 1], {
        extrapolateRight: "clamp",
    });

    // ── 背景波形 ──
    const wave1 = Math.sin(frame * 0.04) * 20;
    const wave2 = Math.cos(frame * 0.03) * 15;

    return (
        <AbsoluteFill
            style={{
                background:
                    "linear-gradient(170deg, #020b1a 0%, #0a1e3a 40%, #132d50 70%, #020b1a 100%)",
                fontFamily,
                overflow: "hidden",
            }}
        >
            {/* 背景波形 */}
            <svg
                style={{ position: "absolute", bottom: 0, left: 0, width: "100%", height: 200 }}
                viewBox="0 0 1920 200"
                preserveAspectRatio="none"
            >
                <path
                    d={`M0 200 Q480 ${130 + wave1} 960 ${150 + wave2} Q1440 ${130 - wave1} 1920 200 Z`}
                    fill="rgba(30, 100, 200, 0.1)"
                />
                <path
                    d={`M0 200 Q480 ${160 + wave2} 960 ${170 - wave1} Q1440 ${160 + wave2} 1920 200 Z`}
                    fill="rgba(30, 100, 200, 0.05)"
                />
            </svg>

            {/* ヘッダーセクション */}
            <div
                style={{
                    position: "absolute",
                    top: 100,
                    left: "50%",
                    transform: `translate(-50%, 0) scale(${interpolate(headerSpring, [0, 1], [0.8, 1])})`,
                    opacity: headerSpring,
                    textAlign: "center",
                }}
            >
                <div
                    style={{
                        fontSize: 72,
                        fontWeight: 900,
                        color: "#ffffff",
                        letterSpacing: 6,
                        textShadow: "0 4px 30px rgba(92,168,232,0.4)",
                    }}
                >
                    この仕事の魅力
                </div>
                <div
                    style={{
                        fontSize: 26,
                        fontWeight: 400,
                        color: "#5ca8e8",
                        letterSpacing: 8,
                        marginTop: 10,
                    }}
                >
                    WHY KAKOGAWA DOBOKU?
                </div>
            </div>

            {/* 魅力リスト */}
            <div
                style={{
                    position: "absolute",
                    top: 310,
                    left: "50%",
                    transform: "translateX(-50%)",
                    display: "flex",
                    flexDirection: "column",
                    gap: 30,
                    width: 1500,
                }}
            >
                <AppealCard
                    icon={<ShieldWaveIcon progress={iconProgress} />}
                    title="街を守るダイナミックな仕事"
                    desc="河川・砂防・治水 ─ 人命を守るインフラの最前線"
                    delay={Math.round(0.4 * fps)}
                    accentColor="#4fc3f7"
                />
                <AppealCard
                    icon={<BridgeLandmarkIcon progress={iconProgress} />}
                    title="完成が目に見える達成感"
                    desc="道路・橋梁・港湾 ─ 地図に残る仕事"
                    delay={Math.round(0.7 * fps)}
                    accentColor="#81c784"
                />
                <AppealCard
                    icon={<CommunityGrowIcon progress={iconProgress} />}
                    title="地域と共に成長できる環境"
                    desc="住民・自治体との連携で社会貢献を実感"
                    delay={Math.round(1.0 * fps)}
                    accentColor="#ffb74d"
                />
            </div>
        </AbsoluteFill>
    );
};

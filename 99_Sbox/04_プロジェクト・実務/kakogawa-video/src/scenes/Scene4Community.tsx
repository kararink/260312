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

// ── マンガ風イラスト：橋の現場 ──
const MangaBridge: React.FC<{ progress: number }> = ({ progress }) => (
    <svg width={280} height={220} viewBox="0 0 280 220">
        {/* 集中線（マンガ風放射） */}
        {Array.from({ length: 16 }, (_, i) => {
            const angle = (i / 16) * Math.PI * 2;
            const x1 = 140 + Math.cos(angle) * 60;
            const y1 = 100 + Math.sin(angle) * 60;
            const x2 = 140 + Math.cos(angle) * 140;
            const y2 = 100 + Math.sin(angle) * 140;
            return (
                <line
                    key={i}
                    x1={x1} y1={y1} x2={x2} y2={y2}
                    stroke="#4fc3f7"
                    strokeWidth={1.5}
                    opacity={progress * 0.15}
                />
            );
        })}
        {/* 橋梁（太線、マンガ風） */}
        <path
            d="M20 140 Q70 60 140 140 Q210 60 260 140"
            fill="none" stroke="#ffffff" strokeWidth={5}
            strokeLinecap="round"
            strokeDasharray={360}
            strokeDashoffset={360 * (1 - progress)}
        />
        {/* 橋脚 */}
        <line x1={70} y1={100} x2={70} y2={180} stroke="#ffffff" strokeWidth={4} opacity={progress} />
        <line x1={140} y1={140} x2={140} y2={180} stroke="#ffffff" strokeWidth={4} opacity={progress} />
        <line x1={210} y1={100} x2={210} y2={180} stroke="#ffffff" strokeWidth={4} opacity={progress} />
        {/* 地面 */}
        <line x1={10} y1={180} x2={270} y2={180} stroke="#4fc3f7" strokeWidth={2} opacity={progress * 0.5} />
        {/* 作業員シルエット（マンガ風） */}
        <g opacity={progress} transform="translate(100, 100)">
            {/* ヘルメット */}
            <ellipse cx={0} cy={-12} rx={8} ry={6} fill="#ffd54f" stroke="#333" strokeWidth={1.5} />
            {/* 顔 */}
            <circle cx={0} cy={-3} r={6} fill="#ffcc80" stroke="#333" strokeWidth={1.5} />
            {/* 体 */}
            <path d="M0 3 L0 22" stroke="#4fc3f7" strokeWidth={3} strokeLinecap="round" />
            <path d="M-10 12 L0 8 L10 12" stroke="#4fc3f7" strokeWidth={2.5} strokeLinecap="round" fill="none" />
            <path d="M0 22 L-8 34 M0 22 L8 34" stroke="#333" strokeWidth={2.5} strokeLinecap="round" />
        </g>
        {/* マンガ吹き出し */}
        <g opacity={progress} transform="translate(160, 55)">
            <ellipse cx={0} cy={0} rx={40} ry={18} fill="white" stroke="#333" strokeWidth={2} />
            <polygon points="-10,16 -5,28 2,17" fill="white" stroke="#333" strokeWidth={2} strokeLinejoin="round" />
            <text x={0} y={5} textAnchor="middle" fontSize={12} fontWeight={900} fill="#333">現場!</text>
        </g>
    </svg>
);

// ── マンガ風イラスト：サイクリング ──
const MangaCycling: React.FC<{ progress: number }> = ({ progress }) => (
    <svg width={280} height={220} viewBox="0 0 280 220">
        {/* スピード線 */}
        {Array.from({ length: 8 }, (_, i) => (
            <line
                key={i}
                x1={10} y1={70 + i * 14}
                x2={10 + 50 * progress} y2={70 + i * 14}
                stroke="#81c784"
                strokeWidth={2}
                opacity={progress * 0.3}
                strokeLinecap="round"
            />
        ))}
        {/* 自転車 */}
        <g transform="translate(140, 120)" opacity={progress}>
            {/* 後輪 */}
            <circle cx={-35} cy={20} r={25} fill="none" stroke="#ffffff" strokeWidth={3} />
            <circle cx={-35} cy={20} r={3} fill="#81c784" />
            {/* 前輪 */}
            <circle cx={35} cy={20} r={25} fill="none" stroke="#ffffff" strokeWidth={3} />
            <circle cx={35} cy={20} r={3} fill="#81c784" />
            {/* フレーム */}
            <path d="M-35 20 L-10 -15 L35 20 M-10 -15 L20 -15 L35 20 M-10 -15 L-35 20" fill="none" stroke="#81c784" strokeWidth={3} strokeLinejoin="round" />
            {/* ハンドル */}
            <path d="M20 -15 L25 -25" stroke="#ffffff" strokeWidth={2.5} strokeLinecap="round" />
            {/* サドル */}
            <line x1={-15} y1={-18} x2={-5} y2={-18} stroke="#333" strokeWidth={3} strokeLinecap="round" />
        </g>
        {/* ライダー */}
        <g opacity={progress} transform="translate(125, 70)">
            <ellipse cx={0} cy={-8} rx={7} ry={5} fill="#4fc3f7" stroke="#333" strokeWidth={1.5} />
            <circle cx={0} cy={0} r={6} fill="#ffcc80" stroke="#333" strokeWidth={1.5} />
            <path d="M0 6 L0 30" stroke="#4fc3f7" strokeWidth={3} strokeLinecap="round" />
            <path d="M0 14 L15 25" stroke="#4fc3f7" strokeWidth={2} strokeLinecap="round" />
            <path d="M0 30 L-10 48 M0 30 L10 48" stroke="#333" strokeWidth={2.5} strokeLinecap="round" />
        </g>
        {/* 河川のイメージ */}
        <path d="M30 190 Q100 178 140 185 Q180 192 250 180" fill="none" stroke="#4fc3f7" strokeWidth={2} opacity={progress * 0.4} strokeLinecap="round" />
        <path d="M30 200 Q100 188 140 195 Q180 202 250 190" fill="none" stroke="#4fc3f7" strokeWidth={1.5} opacity={progress * 0.25} strokeLinecap="round" />
    </svg>
);

// ── マンガ風イラスト：河川整備 ──
const MangaRiver: React.FC<{ progress: number }> = ({ progress }) => (
    <svg width={280} height={220} viewBox="0 0 280 220">
        {/* 集中線 */}
        {Array.from({ length: 12 }, (_, i) => {
            const angle = (i / 12) * Math.PI * 2;
            const x1 = 140 + Math.cos(angle) * 50;
            const y1 = 90 + Math.sin(angle) * 50;
            const x2 = 140 + Math.cos(angle) * 130;
            const y2 = 90 + Math.sin(angle) * 130;
            return (
                <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke="#ba68c8" strokeWidth={1} opacity={progress * 0.12} />
            );
        })}
        {/* 河川 */}
        <path
            d="M0 100 Q70 70 140 100 Q210 130 280 100"
            fill="none" stroke="#4fc3f7" strokeWidth={4}
            strokeDasharray={300}
            strokeDashoffset={300 * (1 - progress)}
            strokeLinecap="round"
        />
        <path
            d="M0 120 Q70 90 140 120 Q210 150 280 120"
            fill="none" stroke="#4fc3f7" strokeWidth={3}
            opacity={progress * 0.5}
            strokeLinecap="round"
        />
        {/* 護岸ブロック */}
        {[40, 80, 120, 160, 200, 240].map((x, i) => (
            <rect key={i} x={x - 8} y={130 + (i % 2) * 5} width={16} height={12} rx={2}
                fill="none" stroke="#90a4ae" strokeWidth={1.5} opacity={progress * 0.6} />
        ))}
        {/* 作業員 */}
        <g opacity={progress} transform="translate(200, 50)">
            <ellipse cx={0} cy={-8} rx={7} ry={5} fill="#ff9800" stroke="#333" strokeWidth={1.5} />
            <circle cx={0} cy={0} r={6} fill="#ffcc80" stroke="#333" strokeWidth={1.5} />
            <path d="M0 6 L0 25" stroke="#ff9800" strokeWidth={3} strokeLinecap="round" />
            <path d="M-10 15 L0 10 L12 18" stroke="#ff9800" strokeWidth={2} strokeLinecap="round" fill="none" />
            <path d="M0 25 L-8 40 M0 25 L8 40" stroke="#333" strokeWidth={2} strokeLinecap="round" />
        </g>
        {/* 吹き出し */}
        <g opacity={progress} transform="translate(80, 40)">
            <rect x={-35} y={-15} width={70} height={28} rx={14} fill="white" stroke="#333" strokeWidth={2} />
            <polygon points="10,13 15,25 22,12" fill="white" stroke="#333" strokeWidth={2} strokeLinejoin="round" />
            <text x={0} y={4} textAnchor="middle" fontSize={11} fontWeight={900} fill="#333">安全第一!</text>
        </g>
        {/* 木 */}
        <g opacity={progress * 0.7} transform="translate(50, 55)">
            <rect x={-3} y={15} width={6} height={15} fill="#795548" rx={2} />
            <circle cx={0} cy={5} r={15} fill="#81c784" opacity={0.7} />
            <circle cx={-8} cy={10} r={10} fill="#66bb6a" opacity={0.5} />
            <circle cx={8} cy={8} r={12} fill="#81c784" opacity={0.6} />
        </g>
    </svg>
);

// フォトカード（マンガイラスト版）
const MangaCard: React.FC<{
    illustration: React.ReactNode;
    title: string;
    desc: string;
    bgColor: string;
    delay: number;
}> = ({ illustration, title, desc, bgColor, delay }) => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const s = spring({
        frame,
        fps,
        delay,
        config: { damping: 10, stiffness: 120 },
    });

    const scale = interpolate(s, [0, 1], [0.85, 1]);
    const y = interpolate(s, [0, 1], [60, 0]);

    return (
        <div
            style={{
                width: 380,
                borderRadius: 24,
                overflow: "hidden",
                transform: `scale(${scale}) translateY(${y}px)`,
                opacity: s,
                position: "relative",
                boxShadow: "0 20px 60px rgba(0,0,0,0.5)",
                border: "3px solid rgba(255,255,255,0.1)",
            }}
        >
            {/* イラスト背景 */}
            <div
                style={{
                    background: bgColor,
                    padding: "20px 0",
                    display: "flex",
                    justifyContent: "center",
                    alignItems: "center",
                    borderBottom: "3px solid rgba(255,255,255,0.08)",
                }}
            >
                {illustration}
            </div>

            {/* テキスト */}
            <div
                style={{
                    padding: "24px 28px",
                    background: "rgba(10,20,40,0.95)",
                }}
            >
                <div
                    style={{
                        fontSize: 30,
                        fontWeight: 900,
                        color: "#ffffff",
                        letterSpacing: 3,
                        marginBottom: 10,
                    }}
                >
                    {title}
                </div>
                <div
                    style={{
                        fontSize: 18,
                        color: "#90a4ae",
                        fontWeight: 400,
                        lineHeight: 1.6,
                    }}
                >
                    {desc}
                </div>
            </div>
        </div>
    );
};

export const Scene4Community: React.FC = () => {
    const frame = useCurrentFrame();
    const { fps } = useVideoConfig();

    const headerSpring = spring({
        frame,
        fps,
        config: { damping: 15, stiffness: 100 },
    });

    const iconProgress = interpolate(frame, [0, 1.5 * fps], [0, 1], {
        extrapolateRight: "clamp",
    });

    return (
        <AbsoluteFill
            style={{
                background:
                    "linear-gradient(150deg, #020b1a 0%, #0a1e3a 50%, #020b1a 100%)",
                fontFamily,
                overflow: "hidden",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                gap: 40,
            }}
        >
            {/* ハーフトーン装飾（マンガの背景） */}
            {Array.from({ length: 40 }, (_, i) => {
                const x = (i % 10) * 200 + 60;
                const y = Math.floor(i / 10) * 300 + 80;
                const size = 3 + (i % 3) * 2;
                return (
                    <div
                        key={i}
                        style={{
                            position: "absolute",
                            left: x,
                            top: y,
                            width: size,
                            height: size,
                            borderRadius: "50%",
                            backgroundColor: "#5ca8e8",
                            opacity: 0.06,
                        }}
                    />
                );
            })}

            {/* ヘッダー */}
            <div
                style={{
                    textAlign: "center",
                    transform: `scale(${interpolate(headerSpring, [0, 1], [0.8, 1])})`,
                    opacity: headerSpring,
                }}
            >
                <div
                    style={{
                        fontSize: 64,
                        fontWeight: 900,
                        color: "#ffffff",
                        letterSpacing: 6,
                        textShadow: "0 4px 30px rgba(92,168,232,0.4)",
                    }}
                >
                    現場のリアル
                </div>
                <div
                    style={{
                        fontSize: 24,
                        fontWeight: 700,
                        color: "#5ca8e8",
                        letterSpacing: 6,
                        marginTop: 8,
                    }}
                >
                    @kakogawadoboku をフォロー
                </div>
            </div>

            {/* マンガ風カード */}
            <div
                style={{
                    display: "flex",
                    gap: 36,
                    justifyContent: "center",
                }}
            >
                <MangaCard
                    illustration={<MangaBridge progress={iconProgress} />}
                    title="橋梁の現場"
                    desc="地域を結ぶ橋の建設・維持管理の最前線"
                    bgColor="linear-gradient(135deg, #0a1e3a 0%, #132d50 100%)"
                    delay={Math.round(0.4 * fps)}
                />
                <MangaCard
                    illustration={<MangaCycling progress={iconProgress} />}
                    title="加古川右岸自転車道"
                    desc="サイクリングマップの企画で地域の魅力を発信"
                    bgColor="linear-gradient(135deg, #0a2a1a 0%, #1a4030 100%)"
                    delay={Math.round(0.7 * fps)}
                />
                <MangaCard
                    illustration={<MangaRiver progress={iconProgress} />}
                    title="河川の景観整備"
                    desc="美しい水辺環境を次世代へつなぐ"
                    bgColor="linear-gradient(135deg, #1a1030 0%, #2a2050 100%)"
                    delay={Math.round(1.0 * fps)}
                />
            </div>
        </AbsoluteFill>
    );
};

import { Composition } from "remotion";
import { KakogawaIntro } from "./KakogawaIntro";

export const RemotionRoot: React.FC = () => {
    return (
        <Composition
            id="KakogawaIntro"
            component={KakogawaIntro}
            durationInFrames={450}
            fps={30}
            width={1920}
            height={1080}
        />
    );
};

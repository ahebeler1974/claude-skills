import React from "react";
import { AbsoluteFill, Audio, Series, staticFile } from "remotion";
import { Scene1, Scene2, Scene3, Scene4, Scene5, Scene6 } from "../scenes/PilotScenes";
import { ProgressIndicator } from "../components/communication";
import roteiro from "../data/roteiro.json";

const FPS = roteiro.meta.fps;
const dur = (id: string) => {
  const c = roteiro.cenas.find((x) => x.id === id)!;
  return Math.round((c.fimSeg - c.inicioSeg) * FPS);
};
export const PILOT_TOTAL_FRAMES =
  dur("s1") + dur("s2") + dur("s3") + dur("s4") + dur("s5") + dur("s6");

export type PilotProps = {
  /** Caminho (relativo a public/) do audio de narracao. Ex.: "audio/narracao.wav". */
  audioSrc?: string;
};

export const HematologiaPilot: React.FC<PilotProps> = ({ audioSrc }) => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#04101c" }}>
      {audioSrc ? <Audio src={staticFile(audioSrc)} /> : null}
      <Series>
        <Series.Sequence durationInFrames={dur("s1")}>
          <Scene1 />
        </Series.Sequence>
        <Series.Sequence durationInFrames={dur("s2")}>
          <Scene2 />
        </Series.Sequence>
        <Series.Sequence durationInFrames={dur("s3")}>
          <Scene3 />
        </Series.Sequence>
        <Series.Sequence durationInFrames={dur("s4")}>
          <Scene4 />
        </Series.Sequence>
        <Series.Sequence durationInFrames={dur("s5")}>
          <Scene5 />
        </Series.Sequence>
        <Series.Sequence durationInFrames={dur("s6")}>
          <Scene6 />
        </Series.Sequence>
      </Series>
      <ProgressIndicator totalFrames={PILOT_TOTAL_FRAMES} />
    </AbsoluteFill>
  );
};

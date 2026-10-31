import React from "react";
import { Composition } from "remotion";
import {
  HematologiaPilot,
  PILOT_TOTAL_FRAMES,
} from "./compositions/HematologiaPilot";
import roteiro from "./data/roteiro.json";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* Piloto vertical 9:16 (YouTube Shorts / TikTok / Reels) */}
      <Composition
        id="HematologiaPilot"
        component={HematologiaPilot}
        durationInFrames={PILOT_TOTAL_FRAMES}
        fps={roteiro.meta.fps}
        width={roteiro.meta.width}
        height={roteiro.meta.height}
        defaultProps={{ audioSrc: undefined as string | undefined }}
      />
      {/*
        Variante 16:9 (futuro): reutilize o mesmo componente mudando width/height
        e ajustando posicoes dos overlays via um contexto de layout. Ex.:
        <Composition id="HematologiaPilot_16x9" ... width={1920} height={1080} />
      */}
    </>
  );
};

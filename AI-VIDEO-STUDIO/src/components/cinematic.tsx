import React from "react";
import {
  AbsoluteFill,
  interpolate,
  random,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { THEME } from "../theme";

/** Fundo escuro cinematografico: gradiente radial azul-profundo + vignette + leve drift. */
export const CinematicBackground: React.FC<{ hue?: number }> = ({ hue = 0 }) => {
  const frame = useCurrentFrame();
  const drift = Math.sin(frame / 90) * 20;
  return (
    <AbsoluteFill
      style={{
        background: `radial-gradient(120% 90% at ${50 + drift / 10}% 35%, ${THEME.bgGlow} 0%, ${THEME.bgMid} 45%, ${THEME.bgDeep} 100%)`,
      }}
    >
      <AbsoluteFill
        style={{
          background:
            "radial-gradient(100% 100% at 50% 50%, rgba(0,0,0,0) 55%, rgba(0,0,0,0.55) 100%)",
        }}
      />
    </AbsoluteFill>
  );
};

/** Brilho suave posicionavel. */
export const GlowEffect: React.FC<{
  x: number;
  y: number;
  size?: number;
  color?: string;
  opacity?: number;
}> = ({ x, y, size = 600, color = THEME.cyan, opacity = 0.35 }) => (
  <div
    style={{
      position: "absolute",
      left: x - size / 2,
      top: y - size / 2,
      width: size,
      height: size,
      borderRadius: "50%",
      background: `radial-gradient(circle, ${color} 0%, rgba(0,0,0,0) 70%)`,
      opacity,
      filter: "blur(8px)",
      pointerEvents: "none",
    }}
  />
);

/** Campo de particulas deterministico (poeira / plasma em suspensao). */
export const ParticleField: React.FC<{
  count?: number;
  color?: string;
  speed?: number;
  seed?: string;
}> = ({ count = 60, color = THEME.cyan, speed = 1, seed = "pf" }) => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      {new Array(count).fill(0).map((_, i) => {
        const px = random(`${seed}-x-${i}`) * width;
        const baseY = random(`${seed}-y-${i}`) * height;
        const drift = (frame * speed * (0.3 + random(`${seed}-s-${i}`))) % height;
        const y = (baseY - drift + height) % height;
        const size = 1.5 + random(`${seed}-r-${i}`) * 3.5;
        const twinkle =
          0.25 + 0.55 * Math.abs(Math.sin(frame / 20 + i));
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: px,
              top: y,
              width: size,
              height: size,
              borderRadius: "50%",
              background: color,
              opacity: twinkle,
              filter: "blur(0.4px)",
            }}
          />
        );
      })}
    </AbsoluteFill>
  );
};

/** Wrapper de camera: zoom + pan + follow via transform. */
export const CameraRig: React.FC<{
  zoomFrom?: number;
  zoomTo?: number;
  panXFrom?: number;
  panXTo?: number;
  panYFrom?: number;
  panYTo?: number;
  durationInFrames: number;
  children: React.ReactNode;
}> = ({
  zoomFrom = 1,
  zoomTo = 1,
  panXFrom = 0,
  panXTo = 0,
  panYFrom = 0,
  panYTo = 0,
  durationInFrames,
  children,
}) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [0, durationInFrames], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  // ease-in-out suave
  const e = p < 0.5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
  const scale = zoomFrom + (zoomTo - zoomFrom) * e;
  const tx = panXFrom + (panXTo - panXFrom) * e;
  const ty = panYFrom + (panYTo - panYFrom) * e;
  return (
    <AbsoluteFill
      style={{
        transform: `translate(${tx}px, ${ty}px) scale(${scale})`,
        transformOrigin: "50% 50%",
      }}
    >
      {children}
    </AbsoluteFill>
  );
};

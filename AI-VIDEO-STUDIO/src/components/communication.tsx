import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { THEME } from "../theme";

/** Titulo animado (entrada com mola + brilho). */
export const AnimatedTitle: React.FC<{
  text: string;
  y?: number;
  size?: number;
  color?: string;
}> = ({ text, y = 360, size = 92, color = THEME.text }) => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const s = spring({ frame, fps, config: { damping: 200 } });
  const opacity = interpolate(frame, [0, 18], [0, 1], { extrapolateRight: "clamp" });
  return (
    <div
      style={{
        position: "absolute",
        top: y,
        width: width - 140,
        left: 70,
        textAlign: "center",
        fontFamily: THEME.fontDisplay,
        fontWeight: 800,
        fontSize: size,
        lineHeight: 1.08,
        color,
        letterSpacing: -1,
        opacity,
        transform: `translateY(${(1 - s) * 40}px)`,
        textShadow: `0 0 28px rgba(34,211,238,0.35)`,
        whiteSpace: "pre-line",
      }}
    >
      {text}
    </div>
  );
};

/** Rotulo cientifico com linha-guia (ex.: "Hemoglobina: ate 4 O2"). */
export const ScientificLabel: React.FC<{
  text: string;
  x: number;
  y: number;
}> = ({ text, x, y }) => {
  const frame = useCurrentFrame();
  const w = interpolate(frame, [0, 14], [0, 1], { extrapolateRight: "clamp" });
  return (
    <div
      style={{
        position: "absolute",
        left: x,
        top: y,
        opacity: w,
        transform: `translateX(${(1 - w) * -20}px)`,
      }}
    >
      <div
        style={{
          fontFamily: THEME.fontBody,
          fontSize: 38,
          fontWeight: 600,
          color: THEME.cyan,
          padding: "10px 20px",
          borderLeft: `4px solid ${THEME.cyan}`,
          background: "rgba(10,47,74,0.5)",
          borderRadius: 6,
          backdropFilter: "blur(2px)",
        }}
      >
        {text}
      </div>
    </div>
  );
};

type Legenda = { t0: number; t1: number; texto: string };

/**
 * Legenda sincronizada. Recebe legendas em segundos ABSOLUTOS e o offset
 * (inicioSeg da cena), convertendo para o frame local da Sequence.
 * AVISO: tempos sao estimados ate re-sincronizar com o audio real.
 */
export const SubtitleOverlay: React.FC<{
  legendas: Legenda[];
  offsetSeg: number;
}> = ({ legendas, offsetSeg }) => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const absSec = offsetSeg + frame / fps;
  const active = legendas.find((l) => absSec >= l.t0 && absSec <= l.t1);
  if (!active) return null;
  const local = (absSec - active.t0) * fps;
  const op = interpolate(local, [0, 6], [0, 1], { extrapolateRight: "clamp" });
  return (
    <div
      style={{
        position: "absolute",
        bottom: 300,
        left: 60,
        width: width - 120,
        textAlign: "center",
        opacity: op,
      }}
    >
      <span
        style={{
          fontFamily: THEME.fontDisplay,
          fontSize: 56,
          fontWeight: 700,
          color: THEME.text,
          lineHeight: 1.25,
          background: THEME.subtitleBg,
          padding: "14px 26px",
          borderRadius: 16,
          boxDecorationBreak: "clone",
          WebkitBoxDecorationBreak: "clone",
          textShadow: "0 2px 10px rgba(0,0,0,0.6)",
        }}
      >
        {active.texto}
      </span>
    </div>
  );
};

/** Barra de progresso fina no topo. */
export const ProgressIndicator: React.FC<{ totalFrames: number }> = ({ totalFrames }) => {
  const frame = useCurrentFrame();
  const { width } = useVideoConfig();
  const w = interpolate(frame, [0, totalFrames], [0, width], { extrapolateRight: "clamp" });
  return (
    <div style={{ position: "absolute", top: 0, left: 0, height: 8, width: w, background: THEME.cyan, opacity: 0.8 }} />
  );
};

/** Card de encerramento com CTA (pergunta). */
export const ClosingCard: React.FC<{ titulo: string; pergunta: string }> = ({ titulo, pergunta }) => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const s = spring({ frame, fps, config: { damping: 200 } });
  return (
    <div
      style={{
        position: "absolute",
        top: 700,
        left: 80,
        width: width - 160,
        textAlign: "center",
        transform: `scale(${0.9 + s * 0.1})`,
        opacity: interpolate(frame, [0, 16], [0, 1], { extrapolateRight: "clamp" }),
      }}
    >
      <div style={{ fontFamily: THEME.fontDisplay, fontSize: 72, fontWeight: 800, color: THEME.text, lineHeight: 1.1 }}>
        {titulo}
      </div>
      <div style={{ marginTop: 40, fontFamily: THEME.fontBody, fontSize: 48, fontWeight: 600, color: THEME.cyan }}>
        {pergunta}
      </div>
    </div>
  );
};

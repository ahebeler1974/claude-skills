import React from "react";
import { interpolate, random, useCurrentFrame } from "remotion";
import { THEME } from "../theme";

function mixColor(a: string, b: string, t: number): string {
  const pa = [parseInt(a.slice(1, 3), 16), parseInt(a.slice(3, 5), 16), parseInt(a.slice(5, 7), 16)];
  const pb = [parseInt(b.slice(1, 3), 16), parseInt(b.slice(3, 5), 16), parseInt(b.slice(5, 7), 16)];
  const r = pa.map((v, i) => Math.round(v + (pb[i] - v) * t));
  return `rgb(${r[0]}, ${r[1]}, ${r[2]})`;
}

/**
 * Hemacia (eritrocito): disco biconcavo, sem nucleo.
 * oxygenation 1 = vermelho vivo (oxi-Hb), 0 = vermelho escuro (desoxi-Hb).
 * NAO muda de FORMA com o O2 (cientificamente correto) — so a cor varia.
 */
export const Hemacia: React.FC<{
  size?: number;
  oxygenation?: number;
  wobble?: boolean;
}> = ({ size = 160, oxygenation = 1, wobble = true }) => {
  const frame = useCurrentFrame();
  const tilt = wobble ? Math.sin(frame / 25) * 6 : 0;
  const rim = mixColor(THEME.bloodDeoxy, THEME.bloodOxy, oxygenation);
  const center = mixColor("#4a0d0b", "#b52520", oxygenation);
  const id = React.useId();
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" style={{ transform: `rotate(${tilt}deg)`, overflow: "visible" }}>
      <defs>
        <radialGradient id={`g-${id}`} cx="50%" cy="42%" r="62%">
          <stop offset="0%" stopColor={center} />
          <stop offset="55%" stopColor={center} />
          <stop offset="72%" stopColor={rim} />
          <stop offset="100%" stopColor={rim} />
        </radialGradient>
        <radialGradient id={`c-${id}`} cx="50%" cy="50%" r="50%">
          <stop offset="0%" stopColor="rgba(0,0,0,0.38)" />
          <stop offset="60%" stopColor="rgba(0,0,0,0.12)" />
          <stop offset="100%" stopColor="rgba(0,0,0,0)" />
        </radialGradient>
      </defs>
      <ellipse cx="50" cy="52" rx="46" ry="30" fill="rgba(0,0,0,0.35)" />
      <ellipse cx="50" cy="50" rx="46" ry="30" fill={`url(#g-${id})`} stroke={rim} strokeWidth="1" />
      {/* depressao central bicôncava */}
      <ellipse cx="50" cy="50" rx="24" ry="15" fill={`url(#c-${id})`} />
      {/* brilho especular */}
      <ellipse cx="34" cy="40" rx="12" ry="6" fill="rgba(255,255,255,0.18)" />
    </svg>
  );
};

/** Molecula de oxigenio O2 (dois atomos ligados). */
export const MoleculaOxigenio: React.FC<{ size?: number; label?: boolean }> = ({
  size = 48,
  label = false,
}) => (
  <svg width={size} height={size} viewBox="0 0 100 60" style={{ overflow: "visible" }}>
    <defs>
      <radialGradient id="o2a" cx="40%" cy="35%" r="65%">
        <stop offset="0%" stopColor="#9be7ff" />
        <stop offset="100%" stopColor={THEME.blue} />
      </radialGradient>
    </defs>
    <rect x="34" y="26" width="32" height="8" rx="4" fill="#9be7ff" opacity="0.8" />
    <circle cx="34" cy="30" r="22" fill="url(#o2a)" />
    <circle cx="66" cy="30" r="22" fill="url(#o2a)" />
    {label && (
      <>
        <text x="34" y="35" fontSize="16" fill="#032033" textAnchor="middle" fontWeight="700">O</text>
        <text x="66" y="35" fontSize="16" fill="#032033" textAnchor="middle" fontWeight="700">O</text>
      </>
    )}
  </svg>
);

/** Hemoglobina simplificada: tetramero (4 subunidades), com sitios de O2. */
export const Hemoglobina: React.FC<{ size?: number; bound?: number }> = ({
  size = 220,
  bound = 4,
}) => {
  const positions = [
    { x: 34, y: 34 },
    { x: 66, y: 34 },
    { x: 34, y: 66 },
    { x: 66, y: 66 },
  ];
  const id = React.useId();
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" style={{ overflow: "visible" }}>
      <defs>
        <radialGradient id={`sub-${id}`} cx="40%" cy="35%" r="70%">
          <stop offset="0%" stopColor="#ff8a85" />
          <stop offset="100%" stopColor={THEME.bloodDeoxy} />
        </radialGradient>
      </defs>
      {positions.map((p, i) => (
        <g key={i}>
          <circle cx={p.x} cy={p.y} r="20" fill={`url(#sub-${id})`} stroke="rgba(0,0,0,0.25)" strokeWidth="1" />
          {/* grupo heme */}
          <circle cx={p.x} cy={p.y} r="6" fill="#2b0605" />
          {/* O2 ligado */}
          {i < bound && <circle cx={p.x + 11} cy={p.y - 11} r="5.5" fill={THEME.cyan} />}
        </g>
      ))}
    </svg>
  );
};

/** Vaso sanguineo: tubo com paredes e leve brilho interno (fundo de cena). */
export const VasoSanguineo: React.FC<{ width: number; height: number; dim?: number }> = ({
  width,
  height,
  dim = 0,
}) => {
  const id = React.useId();
  const wall = interpolate(dim, [0, 1], [0.5, 0.2]);
  return (
    <svg width={width} height={height} viewBox={`0 0 ${width} ${height}`} style={{ position: "absolute" }}>
      <defs>
        <linearGradient id={`v-${id}`} x1="0" y1="0" x2="1" y2="0">
          <stop offset="0%" stopColor={`rgba(123,21,18,${wall})`} />
          <stop offset="50%" stopColor={`rgba(60,10,12,${wall * 0.4})`} />
          <stop offset="100%" stopColor={`rgba(123,21,18,${wall})`} />
        </linearGradient>
      </defs>
      <rect x="0" y="0" width={width} height={height} fill={`url(#v-${id})`} opacity="0.5" />
      <rect x="0" y="0" width="26" height={height} fill="rgba(180,40,36,0.35)" />
      <rect x={width - 26} y="0" width="26" height={height} fill="rgba(180,40,36,0.35)" />
    </svg>
  );
};

/** Rede de capilares: linhas ramificadas deterministicas. */
export const CapilarRede: React.FC<{ width: number; height: number; glow?: number }> = ({
  width,
  height,
  glow = 0.4,
}) => {
  const lines = new Array(10).fill(0).map((_, i) => {
    const x0 = random(`cap-x0-${i}`) * width;
    const y0 = random(`cap-y0-${i}`) * height;
    const x1 = random(`cap-x1-${i}`) * width;
    const y1 = random(`cap-y1-${i}`) * height;
    return { x0, y0, x1, y1, w: 1 + random(`cap-w-${i}`) * 3 };
  });
  return (
    <svg width={width} height={height} viewBox={`0 0 ${width} ${height}`} style={{ position: "absolute" }}>
      {lines.map((l, i) => (
        <line
          key={i}
          x1={l.x0}
          y1={l.y0}
          x2={l.x1}
          y2={l.y1}
          stroke={THEME.bloodOxy}
          strokeWidth={l.w}
          opacity={glow}
          strokeLinecap="round"
        />
      ))}
    </svg>
  );
};

/** Celula humana generica (com membrana, citoplasma e mitocondria). */
export const CelulaGenerica: React.FC<{ size?: number; energy?: number }> = ({
  size = 420,
  energy = 1,
}) => {
  const id = React.useId();
  const frame = useCurrentFrame();
  const mitoGlow = interpolate(energy, [0, 1], [0.15, 0.85]);
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" style={{ overflow: "visible" }}>
      <defs>
        <radialGradient id={`cell-${id}`} cx="50%" cy="45%" r="60%">
          <stop offset="0%" stopColor="rgba(45,212,191,0.28)" />
          <stop offset="100%" stopColor="rgba(10,47,74,0.5)" />
        </radialGradient>
      </defs>
      <circle cx="50" cy="50" r="46" fill={`url(#cell-${id})`} stroke={THEME.teal} strokeWidth="1.2" opacity="0.9" />
      <circle cx="42" cy="46" r="14" fill="rgba(34,211,238,0.22)" stroke={THEME.cyan} strokeWidth="1" />
      {/* mitocondrias */}
      {[{ x: 64, y: 40 }, { x: 60, y: 64 }, { x: 36, y: 68 }].map((m, i) => (
        <ellipse
          key={i}
          cx={m.x}
          cy={m.y}
          rx="9"
          ry="5"
          fill={THEME.cyan}
          opacity={mitoGlow * (0.6 + 0.4 * Math.abs(Math.sin(frame / 15 + i)))}
        />
      ))}
    </svg>
  );
};

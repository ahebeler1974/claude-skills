import React from "react";
import {
  AbsoluteFill,
  interpolate,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { THEME } from "../theme";
import {
  CameraRig,
  CinematicBackground,
  GlowEffect,
  ParticleField,
} from "../components/cinematic";
import {
  CapilarRede,
  CelulaGenerica,
  Hemacia,
  Hemoglobina,
  MoleculaOxigenio,
  VasoSanguineo,
} from "../components/scientific";
import {
  AnimatedTitle,
  ClosingCard,
  ScientificLabel,
  SubtitleOverlay,
} from "../components/communication";
import roteiro from "../data/roteiro.json";

const C = Object.fromEntries(roteiro.cenas.map((c) => [c.id, c]));

/** Fade de entrada/saida padrao da cena. */
const SceneFade: React.FC<{ dur: number; children: React.ReactNode }> = ({ dur, children }) => {
  const frame = useCurrentFrame();
  const op = interpolate(frame, [0, 12, dur - 12, dur], [0, 1, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return <AbsoluteFill style={{ opacity: op }}>{children}</AbsoluteFill>;
};

/** Fluxo de hemacias atravessando a tela. */
const FluxoHemacias: React.FC<{ n?: number; oxygenation?: number; speed?: number }> = ({
  n = 5,
  oxygenation = 1,
  speed = 2.2,
}) => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();
  return (
    <>
      {new Array(n).fill(0).map((_, i) => {
        const laneY = (height / (n + 1)) * (i + 1) + Math.sin(frame / 18 + i) * 24;
        const x = ((frame * speed + i * 260) % (width + 320)) - 160;
        const size = 130 + (i % 3) * 30;
        return (
          <div key={i} style={{ position: "absolute", left: x, top: laneY - size / 2 }}>
            <Hemacia size={size} oxygenation={oxygenation} />
          </div>
        );
      })}
    </>
  );
};

export const Scene1: React.FC = () => {
  const { width, height } = useVideoConfig();
  const dur = (C.s1.fimSeg - C.s1.inicioSeg) * 30;
  return (
    <SceneFade dur={dur}>
      <CinematicBackground />
      <VasoSanguineo width={width} height={height} dim={0.3} />
      <CameraRig zoomFrom={1.05} zoomTo={1.18} panYFrom={0} panYTo={-30} durationInFrames={dur}>
        <FluxoHemacias n={5} oxygenation={1} />
      </CameraRig>
      <ParticleField count={70} color={THEME.cyan} speed={1.2} />
      <GlowEffect x={width / 2} y={height * 0.3} size={760} color={THEME.cyan} opacity={0.22} />
      <AnimatedTitle text={C.s1.textoTela.replace(/\\n/g, "\n")} y={430} size={96} />
      <SubtitleOverlay legendas={C.s1.legendas} offsetSeg={C.s1.inicioSeg} />
    </SceneFade>
  );
};

export const Scene2: React.FC = () => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();
  const dur = (C.s2.fimSeg - C.s2.inicioSeg) * 30;
  // O2 ligando progressivamente (0 -> 4)
  const bound = Math.min(4, Math.floor(interpolate(frame, [40, 180], [0, 4.99], { extrapolateLeft: "clamp", extrapolateRight: "clamp" })));
  return (
    <SceneFade dur={dur}>
      <CinematicBackground />
      <ParticleField count={50} color={THEME.blue} speed={0.8} seed="s2" />
      <CameraRig zoomFrom={1} zoomTo={1.35} durationInFrames={dur}>
        <AbsoluteFill style={{ alignItems: "center", justifyContent: "center" }}>
          <Hemoglobina size={620} bound={bound} />
        </AbsoluteFill>
      </CameraRig>
      <GlowEffect x={width / 2} y={height / 2} size={900} color={THEME.bloodOxy} opacity={0.18} />
      {/* O2 chegando */}
      {[0, 1, 2].map((i) => {
        const p = ((frame + i * 40) % dur) / dur;
        return (
          <div key={i} style={{ position: "absolute", left: interpolate(p, [0, 1], [width + 60, width / 2 - 20]), top: height * (0.3 + i * 0.12) }}>
            <MoleculaOxigenio size={70} label />
          </div>
        );
      })}
      <ScientificLabel text={C.s2.textoTela} x={90} y={height * 0.2} />
      <SubtitleOverlay legendas={C.s2.legendas} offsetSeg={C.s2.inicioSeg} />
    </SceneFade>
  );
};

export const Scene3: React.FC = () => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();
  const dur = (C.s3.fimSeg - C.s3.inicioSeg) * 30;
  const dim = interpolate(frame, [0, dur], [0.2, 0.85], { extrapolateRight: "clamp" });
  const oxy = interpolate(frame, [0, dur], [0.9, 0.4], { extrapolateRight: "clamp" });
  return (
    <SceneFade dur={dur}>
      <CinematicBackground />
      <VasoSanguineo width={width} height={height} dim={dim} />
      <CapilarRede width={width} height={height} glow={interpolate(dim, [0.2, 0.85], [0.5, 0.15])} />
      <CameraRig zoomFrom={1.1} zoomTo={1} panXFrom={-20} panXTo={20} durationInFrames={dur}>
        <FluxoHemacias n={4} oxygenation={oxy} speed={1.4} />
      </CameraRig>
      <AbsoluteFill style={{ background: `rgba(2,8,16,${interpolate(dim, [0.2, 0.85], [0, 0.45])})` }} />
      <ScientificLabel text={C.s3.textoTela} x={70} y={height * 0.16} />
      <SubtitleOverlay legendas={C.s3.legendas} offsetSeg={C.s3.inicioSeg} />
    </SceneFade>
  );
};

export const Scene4: React.FC = () => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();
  const dur = (C.s4.fimSeg - C.s4.inicioSeg) * 30;
  // pulso (batimento): escala sutil ritmica
  const beat = 1 + Math.sin(frame / 7) * 0.02;
  return (
    <SceneFade dur={dur}>
      <CinematicBackground />
      <AbsoluteFill style={{ transform: `scale(${beat})`, transformOrigin: "50% 50%" }}>
        <CapilarRede width={width} height={height} glow={0.6} />
      </AbsoluteFill>
      <FluxoHemacias n={6} oxygenation={0.7} speed={3.4} />
      <ParticleField count={60} color={THEME.teal} speed={2} seed="s4" />
      {[0, 1, 2, 3].map((i) => {
        const p = ((frame * 2.4 + i * 70) % (height + 120)) - 60;
        return (
          <div key={i} style={{ position: "absolute", left: width * (0.2 + i * 0.18), top: p }}>
            <MoleculaOxigenio size={56} />
          </div>
        );
      })}
      <GlowEffect x={width / 2} y={height / 2} size={820} color={THEME.teal} opacity={0.16} />
      <ScientificLabel text={C.s4.textoTela} x={70} y={height * 0.14} />
      <SubtitleOverlay legendas={C.s4.legendas} offsetSeg={C.s4.inicioSeg} />
    </SceneFade>
  );
};

export const Scene5: React.FC = () => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();
  const dur = (C.s5.fimSeg - C.s5.inicioSeg) * 30;
  const energy = interpolate(frame, [0, dur], [0.95, 0.25], { extrapolateRight: "clamp" });
  return (
    <SceneFade dur={dur}>
      <CinematicBackground />
      <ParticleField count={36} color={THEME.cyan} speed={0.5} seed="s5" />
      <CameraRig zoomFrom={1} zoomTo={1.18} durationInFrames={dur}>
        <AbsoluteFill style={{ alignItems: "center", justifyContent: "center" }}>
          <CelulaGenerica size={760} energy={energy} />
        </AbsoluteFill>
      </CameraRig>
      <AbsoluteFill style={{ background: `rgba(2,8,16,${interpolate(frame, [0, dur], [0, 0.35], { extrapolateRight: "clamp" })})` }} />
      <ScientificLabel text={C.s5.textoTela} x={70} y={height * 0.16} />
      <SubtitleOverlay legendas={C.s5.legendas} offsetSeg={C.s5.inicioSeg} />
    </SceneFade>
  );
};

export const Scene6: React.FC = () => {
  const { width, height } = useVideoConfig();
  const dur = (C.s6.fimSeg - C.s6.inicioSeg) * 30;
  return (
    <SceneFade dur={dur}>
      <CinematicBackground />
      <ParticleField count={60} color={THEME.cyan} speed={1} seed="s6" />
      <CameraRig zoomFrom={1.25} zoomTo={1} durationInFrames={dur}>
        <AbsoluteFill style={{ alignItems: "center", justifyContent: "flex-start", paddingTop: height * 0.18 }}>
          <Hemacia size={300} oxygenation={1} />
        </AbsoluteFill>
      </CameraRig>
      <GlowEffect x={width / 2} y={height * 0.28} size={700} color={THEME.cyan} opacity={0.22} />
      <ClosingCard titulo={C.s6.textoTela} pergunta="Qual resposta do corpo mais te surpreendeu?" />
      <SubtitleOverlay legendas={C.s6.legendas} offsetSeg={C.s6.inicioSeg} />
    </SceneFade>
  );
};

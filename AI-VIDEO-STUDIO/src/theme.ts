/**
 * Identidade visual do estudio (tokens reutilizaveis).
 * Trocar estes valores muda o visual de TODOS os videos.
 */
export const THEME = {
  // Fundo escuro / azul-profundo
  bgDeep: "#04101c",
  bgMid: "#061a2b",
  bgGlow: "#0a2f4a",

  // Acentos: ciano, azul, verde-agua
  cyan: "#22d3ee",
  blue: "#3b82f6",
  blueDark: "#1e3a8a",
  teal: "#2dd4bf",

  // Sangue: oxigenado (vermelho vivo) -> desoxigenado (vermelho escuro)
  // (Cientificamente correto: desoxi-hemoglobina e vermelho ESCURO, nao azul.)
  bloodOxy: "#ef3b3b",
  bloodDeoxy: "#7a1512",

  // Texto
  text: "#e8f6ff",
  textMuted: "#9fb6c7",
  subtitleBg: "rgba(3, 12, 22, 0.72)",

  // Tipografia (system stack para nao depender de rede; troque por @remotion/google-fonts se quiser)
  fontDisplay:
    '"Inter", "Segoe UI", system-ui, -apple-system, Roboto, Helvetica, Arial, sans-serif',
  fontBody:
    '"Inter", "Segoe UI", system-ui, -apple-system, Roboto, Helvetica, Arial, sans-serif',
} as const;

export const VIDEO = {
  width: 1080,
  height: 1920,
  fps: 30,
} as const;

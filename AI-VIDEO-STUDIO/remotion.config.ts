import { Config } from "@remotion/cli/config";

// Codec e qualidade (H.264 + AAC quando houver audio no render).
Config.setVideoImageFormat("jpeg");
Config.setCodec("h264");
Config.setConcurrency(4); // 4 vCPUs neste ambiente; ajuste na sua maquina.

// Sem GPU neste ambiente -> renderizador de software (swiftshader) e o padrao seguro.
// Em maquina com GPU, voce pode remover/alterar esta linha para acelerar.
Config.setChromiumOpenGlRenderer("swangle");

// IMPORTANTE: evitamos baixar o Chrome proprio do Remotion usando o Chrome do sistema.
// O caminho e passado via flag --browser-executable nos scripts do package.json.

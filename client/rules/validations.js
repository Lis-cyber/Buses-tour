export default {
  req: [(v) => !!v || "Campo requerido"],
  input_text_required: [
    (v) => {
      if (!v) {
        ("Campo requerido");
      } else if (
        /['¿!@#$\^&%*\(\)+=\[\]\/{}|<>?`´"©✓®°×∆~€£¥•:;”’_\\;√π÷¶™¢+0-9_+]/.test(v)
      ) {
        return "Caracter no válido";
      } else if (v.trim().length < 0) {
        return "Campo requerido";
      } else {
        return true;
      }
    },
  ],

  input_text: [
    (v) =>
      !/['¿!@#$\^&%*\(\)+=\[\]\/{}|<>?`´"©✓®°×∆~€£¥•:;”’_\\;√π÷¶™¢]/.test(v) ||
      "Caracter no válido" ,
  ],
  email: [
    v => /^[a-zA-Z0-9_+&*-]+(?:\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7}$/.test(v) || 'No es un correo electrónico válido',
  ],
  required: [
    (v) => {
      if (v.trim) {
        if (!v || v.trim().length === 0) {
          return "Campo requerido";
        }
      } else {
        if (!v || v.length === 0) {
          return "Campo requerido";
        }
      }
      if (v < 1) {
        return "Número inválido";
      }
      return true;
    },
  ],
};

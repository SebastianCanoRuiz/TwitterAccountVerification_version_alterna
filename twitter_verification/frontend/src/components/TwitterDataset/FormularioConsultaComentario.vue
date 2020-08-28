<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Consultar veracidad cuenta de Twitter basado en un comentario</h2>
            </div>
        </div>

        <div class="row">
            <div class="col">
                <div class="card">
                    <div class="card-body">
                        <form @submit="onSubmit">
                            <div class="form-group row">
                                <label for="title" class="col-sm-2 col-form-label">Comentario</label>
                                <div class="col-sm-6">
                                    <textarea name="comentario" class="form-control" placeholder="Ingrese un comentario..." rows="3" v-model="comentario"></textarea>
                                </div>
                            </div>

                            <div class="rows">
                                <div class="col text-left">
                                    <b-button class="form-control my-2 w-25" type="submit" variant="primary">Consultar</b-button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
</template>

<script>
import axios from "axios";
//import swal from "seetelart";

export default {
  data() {
    return {
      //Dato del imput del TextArea
      comentario: "",
      perfil: "",
      cantidad_palabras: 9, //
      comentarios_repetidos: 0, //
      insultos: 0, //
      emoticones: 0,
      multimedia: 0,
      links: 0, //
      comentarios_raros: 0,
      label: "",
      dataset: [],
      lista_insultos: [
        { insulto: "rata", numero: "1" },
        { insulto: "hampom", numero: "2" },
        { insulto: "culo", numero: "3" },
        { insulto: "bruto", numero: "4" },
        { insulto: "inmmable", numero: "5" },
        { insulto: "mierda", numero: "6" },
        { insulto: "asco", numero: "7" },
        { insulto: "ridiculo", numero: "8" },
        { insulto: "gueva", numero: "9" },
        { insulto: "asqueroso", numero: "10" },
        { insulto: "pendejo", numero: "11" },
        { insulto: "hijueputa", numero: "12" },
        { insulto: "hpts", numero: "13" },
        { insulto: "hp", numero: "14" },
        { insulto: "hpta", numero: "15" },
        { insulto: "hijodeputa", numero: "16" },
        { insulto: "triplehpta", numero: "17" },
        { insulto: "ifueputa", numero: "18" },
        { insulto: "hijo de perra", numero: "19" },
        { insulto: "vieja catrehijueputa", numero: "20" },
        { insulto: "hdp", numero: "21" },
        { insulto: "basura", numero: "22" },
        { insulto: "vandido", numero: "23" },
        { insulto: "bandido", numero: "24" },
        { insulto: "bandida", numero: "25" },
        { insulto: "malparido", numero: "26" },
        { insulto: "mp", numero: "27" },
        { insulto: "malnacidos", numero: "28" },
        { insulto: "perra", numero: "29" },
        { insulto: "estupidez", numero: "30" },
        { insulto: "loca", numero: "31" },
        { insulto: "lava cucos", numero: "32" },
        { insulto: "mamertos", numero: "33" },
        { insulto: "maricas", numero: "34" },
        { insulto: "mk", numero: "35" },
        { insulto: "mkda", numero: "36" },
        { insulto: "mariquita", numero: "37" },
        { insulto: "petardo", numero: "38" },
        { insulto: "puto", numero: "39" },
        { insulto: "puta", numero: "40" },
        { insulto: "perro", numero: "41" },
        { insulto: "bobo", numero: "42" },
        { insulto: "repirobo", numero: "43" },
        { insulto: "paja", numero: "44" },
        { insulto: "ramplom", numero: "45" },
        { insulto: "jeton", numero: "46" },
        { insulto: "pendejadas", numero: "47" },
        { insulto: "cara de orinal", numero: "48" },
        { insulto: "desgraciado", numero: "49" },
        { insulto: "bocon", numero: "50" },
        { insulto: "cagarle", numero: "51" },
        { insulto: "mk", numero: "52" },
        { insulto: "cabron", numero: "53" },
        { insulto: "escremento", numero: "54" },
        { insulto: "depravado", numero: "55" },
        { insulto: "jodas", numero: "56" },
        { insulto: "joda", numero: "57" },
        { insulto: "maldita", numero: "58" },
        { insulto: "genocida", numero: "59" },
        { insulto: "asesina", numero: "60" },
        { insulto: "terrorista", numero: "61" },
        { insulto: "gamberro", numero: "62" },
        { insulto: "narcoterroristas", numero: "63" },
        { insulto: "izquierdosas", numero: "64" },
        { insulto: "corruptas", numero: "65" },
        { insulto: "corruptos", numero: "66" },
        { insulto: "ass", numero: "67" },
        { insulto: "maldito", numero: "68" },
        { insulto: "imbecil", numero: "69" },
        { insulto: "vagabunda", numero: "70" },
        { insulto: "pendeja", numero: "71" },
        { insulto: "babosada", numero: "72" },
        { insulto: "porqueria", numero: "73" },
        { insulto: "sinverguenza", numero: "74" },
        { insulto: "guerristas", numero: "75" },
        { insulto: "desagradable", numero: "76" },
        { insulto: "horrible", numero: "77" },
        { insulto: "idiota", numero: "78" },
        { insulto: "payasada", numero: "79" },
        { insulto: "miserable", numero: "80" },
        { insulto: "mamerta", numero: "81" },
        { insulto: "carajo", numero: "82" },
        { insulto: "estupida", numero: "83" },
        { insulto: "majadera", numero: "84" },
        { insulto: "dejenerada", numero: "85" },
        { insulto: "cochina", numero: "86" },
        { insulto: "nepe", numero: "87" },
        { insulto: "guerrillera", numero: "88" },
        { insulto: "maldita", numero: "89" },
        { insulto: "malditos", numero: "90" },
        { insulto: "paracos", numero: "91" },
        { insulto: "ladrones", numero: "92" },
        { insulto: "ladron", numero: "93" },
        { insulto: "estupido", numero: "94" },
        { insulto: "troglodita", numero: "95" },
        { insulto: "picaro", numero: "96" },
        { insulto: "ratero", numero: "97" },
        { insulto: "paramilitares", numero: "98" },
        { insulto: "bufon", numero: "99" },
        { insulto: "uribertos", numero: "100" },
        { insulto: "gata", numero: "101" },
        { insulto: "tangvones", numero: "102" },
        { insulto: "bollo", numero: "103" },
        { insulto: "bobasos", numero: "104" },
        { insulto: "bobos", numero: "105" },
        { insulto: "comamierda", numero: "106" },
        { insulto: "pudricion", numero: "107" },
        { insulto: "burradas", numero: "108" },
        { insulto: "ineptos", numero: "109" },
        { insulto: "gonorrea", numero: "110" },
        { insulto: "escoria", numero: "111" },
        { insulto: "babosa", numero: "112" },
        { insulto: "duquemiserable", numero: "113" },
        { insulto: "ganaronlosincompetentes", numero: "114" },
        { insulto: "farsantos", numero: "115" },
        { insulto: "castrochavistas", numero: "116" },
        { insulto: "sonsos", numero: "117" },
        { insulto: "chambones", numero: "118" },
        { insulto: "desmierde", numero: "119" },
        { insulto: "cagadas", numero: "120" },
        { insulto: "inutil", numero: "121" },
        { insulto: "uribestias", numero: "122" },
        { insulto: "adefecio", numero: "123" },
        { insulto: "rastreros", numero: "124" },
        { insulto: "medios(cres)", numero: "125" },
        { insulto: "mal nacidos", numero: "126" },
        { insulto: "ampones", numero: "127" },
        { insulto: "cafre", numero: "128" },
        { insulto: "retrogrado", numero: "129" },
        { insulto: "weon", numero: "130" },
        { insulto: "bruja", numero: "131" },
        { insulto: "zorra", numero: "132" },
        { insulto: "burro", numero: "133" },
        { insulto: "pelmazo", numero: "134" },
        { insulto: "caresapo", numero: "135" },
        { insulto: "trafuga", numero: "136" },
        { insulto: "pelele", numero: "137" },
        { insulto: "patetico", numero: "138" },
        { insulto: "despreciable", numero: "139" },
        { insulto: "titere", numero: "140" },
        { insulto: "malandros", numero: "141" },
        { insulto: "pecueca", numero: "142" },
        { insulto: "pocilgas", numero: "143" },
        { insulto: "narcoparauribismo", numero: "144" },
        { insulto: "cerdo", numero: "145" },
        { insulto: "fastidio", numero: "146" },
        { insulto: "jibaro", numero: "147" },
        { insulto: "brutalidad", numero: "148" },
        { insulto: "alimaña", numero: "149" },
        { insulto: "sangano", numero: "150" },
        { insulto: "sanguijuela", numero: "151" },
        { insulto: "petrocarroñero", numero: "152" },
        { insulto: "jodiendo", numero: "153" },
        { insulto: "njd", numero: "154" },
        { insulto: "jeta", numero: "155" },
        { insulto: "petrogueva", numero: "156" },
        { insulto: "tipejo", numero: "157" },
        { insulto: "lacra", numero: "158" },
        { insulto: "mequetrefe", numero: "159" },
        { insulto: "odioso", numero: "160" },
        { insulto: "maracachafa", numero: "161" },
        { insulto: "embrutecio", numero: "162" },
        { insulto: "lunatico", numero: "163" },
        { insulto: "wtf", numero: "164" },
        { insulto: "canalla", numero: "165" },
        { insulto: "cinico", numero: "166" },
        { insulto: "demente", numero: "167" },
        { insulto: "piromano", numero: "168" },
        { insulto: "atolondrados", numero: "169" },
        { insulto: "orate", numero: "170" },
        { insulto: "energumeno", numero: "171" },
        { insulto: "chimbear", numero: "172" },
        { insulto: "mamada", numero: "173" },
        { insulto: "bagazo", numero: "174" },
        { insulto: "monda", numero: "175" },
        { insulto: "marrano", numero: "176" },
        { insulto: "calaña", numero: "177" },
        { insulto: "oligarcas", numero: "178" },
        { insulto: "sapo", numero: "179" },
        { insulto: "cagadisimos", numero: "180" },
        { insulto: "cabrones", numero: "181" },
        { insulto: "parasitos", numero: "182" },
        { insulto: "piltrafa", numero: "183" },
        { insulto: "mamarracho", numero: "184" },
        { insulto: "fea", numero: "185" },
        { insulto: "malagradecido", numero: "186" },
        { insulto: "pusilanime", numero: "187" },
        { insulto: "incompetencia", numero: "188" },
        { insulto: "webon", numero: "189" },
        { insulto: "patrañoso", numero: "190" },
        { insulto: "zoquete", numero: "191" },
        { insulto: "inservible", numero: "192" },
        { insulto: "bobote", numero: "193" },
        { insulto: "jedionda", numero: "194" },
        { insulto: "bestia", numero: "195" },
        { insulto: "sandeces", numero: "196" },
        { insulto: "malcriado", numero: "197" },
        { insulto: "porky", numero: "198" },
        { insulto: "chimbas", numero: "199" },
        { insulto: "impedido", numero: "200" },
        { insulto: "gordo teton", numero: "201" },
      ],
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();
      //var respuesta = [];
      //this.consultarDatasetCompleto(evt);

      //Validacion para el campo cantidad_palabras
      this.contarPalabras(this.comentario);
      //this.tieneComentarios_repetidos();
      //this.tieneInsultosLinks();

      // var primerBlanco = /^ /;
      // var ultimoBlanco = / $/;
      // var variosBlancos = /[ ]+/g;

      // this.comentario = this.comentario.replace(variosBlancos, " ");
      // this.comentario = this.comentario.replace(primerBlanco, "");
      // this.comentario = this.comentario.replace(ultimoBlanco, "");
      // var textoTroceado = this.comentario.split(this.comentario, " ");
      // this.cantidad_palabras = textoTroceado.length;



      // console.log(typeof this.comentario);
      // console.log(this.cantidad_palabras);




      //var path = //`http://localhost:8000/api/datos-twitter/${this.cantidad_palabras}/${this.comentarios_repetidos}/${this.insultos}/${this.emoticones}/${this.multimedia}`;
      var path = `http://localhost:8000/api/datos-twitter/${this.cantidad_palabras}/`;

      axios
        .get(path, { responseType: "json" })
        .then((response) => {
          //respuesta = [ ...response.data];
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    consultarDatasetCompleto(evt) {
      evt.preventDefault();

      axios
        .get(`http://localhost:8000/api/dataset/`, { responseType: "json" })
        .then((response) => {
          this.dataset = response.data;
          
          for (var i = 0; i < 9; i++) {
            n += i;
            mifuncion(n);
          }


        })
        .catch((error) => {
          console.log(error);
        });
    },

    //Metodo que se encarga de contar las palabras de un comentario
    contarPalabras(coment) {
      this.cantidad_palabras = coment.split(" ").length;
    },

    tieneComentarios_repetidos() {
      for (var i = 0; i < this.dataset.length; i++) {
        if (this.comentario == this.dataset[i].comentario) {
          this.comentarios_repetidos = 1;
          break;
        }
      }
    },

    tieneInsultosLinks() {
      var arregloPalabras = this.comentario.split(" ");

      for (var i = 0; i < arregloPalabras.length; i++) {
        if (arregloPalabras[i].startsWith("http")) {
          this.comentarios_repetidos = 1;
          break;
        }
      }

      for (var i = 0; i < arregloPalabras.length; i++) {
        if (!isNaN(this.lista_insultos[arregloPalabras[i]])) {
          this.insultos = 1;
          break;
        }
      }
    },
  },
};
</script>

<style>
</style>
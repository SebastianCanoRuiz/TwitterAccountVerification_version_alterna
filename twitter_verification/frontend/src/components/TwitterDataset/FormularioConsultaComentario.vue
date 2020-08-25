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
                                    <textarea name="comentario" class="form-control" placeholder="Ingrese un comentario..." rows="3" v-model.trim="form.comentario"></textarea>
                                </div>
                            </div>

                            <div class="rows">
                                <div class="col text-left">
                                    <b-button type="submit" variant="primary">Consultar</b-button>
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
      form: {
        cant: 3000,
      },
    };
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault();

      const path = "http://localhost:8000/api/v1.0/DatosComentarios/";

      axios
        .post(path, {
            comentario: this.form.comentario,
            cantidad: 3000
        }).then((response) => {
            console.log('Alguito');
        })
        .catch((error) => {
          console.log(error);
        });
    },

    // getDatos() {
    //   const path = "http://localhost:8000/api/v1.0/DatosComentarios/";

    //   axios
    //     .get(path)
    //     .then((response) => {
    //       this.form.comentario = response.data.length;
    //     })
    //     .catch((error) => {
    //       console.log(error);
    //     });
    // },

    //Metodo que se encarga de contar las palabras de un comentario
    // contarPalabras (coment) {
    //   primerBlanco = /^ /;
    //   ultimoBlanco = / $/;
    //   variosBlancos = /[ ]+/g;

    //   coment = coment.replace(variosBlancos, " ");
    //   coment = coment.replace(primerBlanco, "");
    //   coment = coment.replace(ultimoBlanco, "");
    //   textoTroceado = coment.split(coment, " ");
    //   cant = textoTroceado.length;
    // },
  },

  /*

            //Consulta para recomendaciones
            path = `http://localhost:8000/api/v2/songs-genre-mood/${this.respuesta[0].video_type}/${this.respuesta[0].predicted_moods}/`;
            axios
              .get(path, { responseType: "json" })
              .then(response => {
                this.generarRecomedaciones(response);
                this.generarAlerta(1);
              })
              .catch(error => {
                console.log("011R-->" + error);
              });

*/
  created() {
  },
};
</script>

<style>
</style>
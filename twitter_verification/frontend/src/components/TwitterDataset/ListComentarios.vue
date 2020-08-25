<template>
  <div class="class container">
      <div class="row">
          <div class="col text-left">
              <h2>Listado de Comentarios</h2>

              <div class="col-md-12">
                  <b-table stripped hover :items="dataset" :fields="fields">
                  </b-table>
              </div>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data () {
        return {
            fields: [
                { key: 'id', label: 'ID'},
                { key: 'perfil', label: 'Perfil'},
                { key: 'comentario', label: 'Comentario'},
                { key: 'cantidad_palabras', label: 'Cant Palabras'},
                { key: 'comentarioa_repetidos', label: 'Comentarios Repetidos'},
                { key: 'insultos', label: 'Insultos'},
                { key: 'emoticones', label: 'Emoticones'},
                { key: 'multimedia', label: 'Multimedia'},
                { key: 'links', label: 'Links'},
                { key: 'comentarios_raros', label: 'Comentarios Raros'},
                { key: 'label', label: 'Etiqueta'}
            ],
            dataset: []

        }
    },
    methods: {
        
        getDatos() {
            const path = 'http://localhost:8000/api/dataset/'
            axios.get(path).then((response) => {
                this.dataset = response.data
            })
            .catch((error) => {
                console.log(error)
            })
        }
    },

    created(){
        this.getDatos()
    }

}
</script>

<style>

</style>
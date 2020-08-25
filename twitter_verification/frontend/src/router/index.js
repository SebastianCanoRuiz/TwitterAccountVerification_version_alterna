import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import ListComentarios from '@/components/TwitterDataset/ListComentarios'
import FormularioConsultaComentario from '@/components/TwitterDataset/FormularioConsultaComentario'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/dataset',
      name: 'ListComentarios',
      component: ListComentarios
    },
    {
      path: '/dataset/consulta',
      name: 'FormularioConsultaComentario',
      component: FormularioConsultaComentario
    }
  ],
  mode: 'history'
})

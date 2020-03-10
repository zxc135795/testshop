import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Search from '../views/Search.vue'
import Category from '../views/Category.vue'
import Mine from '../views/Mine.vue'
import UserShow from '../views/UserShow.vue'
import Cart from '../views/Cart.vue'
import Detail from '../views/Detail.vue'
import Daoh from '../components/Daoh.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
	meta:{
		tabbar:true
	},
  },
  {
    path: '/daoh',
    name: 'daoh',
    component: Daoh,
  	meta:{
  		tabbar:true
  	},
},
  {
    path: '/detail',
    name: 'detail',
    component: Detail
  },
  {
    path: '/cart',
    name: 'cart',
    component: Cart,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/usershow',
    name: 'usershow',
    component: UserShow,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/search',
    name: 'search',
    component: Search,
	
  },
  {
    path: '/category',
    name: 'category',
    component: Category,
	meta:{
		tabbar:true
	}
  },
  {
    path: '/mine',
    name: 'mine',
    
    component:Mine,
	meta:{
		tabbar:true
	}
  }
]

const router = new VueRouter({
  routes,
  // 路由异步滚动,添加事件scrollBehavior,参数to from savedPosition ,返回刷新跳转位置
  
  // mode:'history',
  // base: process.env.BASE_URL,
  scrollBehavior (to, from, savedPosition) {
      return {x:0,y:0 }
    }
})

export default router

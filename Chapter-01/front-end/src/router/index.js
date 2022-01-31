import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: "/",
        name: "sign-in",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(/* webpackChunkName: "sign-in" */ "../views/sign-in")
    },
    {
        path: "/auth/sign-up",
        name: "sign-up",
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import(/* webpackChunkName: "sign-up" */ "../views/sign-up")
    },
    {
        path: "/home",
        name: "home",
        component: () => import(/* webpackChunkName: "home" */ "../views/Home")
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router

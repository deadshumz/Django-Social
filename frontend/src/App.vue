<template lang="">
    <div class="bg-gray-50 min-h-screen">
        <div class="container max-w-sm min-h-screen flex items-center justify-center mx-auto">
            <form class="w-full p-5 bg-white border p-5">
                <h1 class="text-3xl font-semibold text-center">Django Social</h1>
                <input type="text" class="block outline-none border border-grey-light w-full p-2 rounded mt-5" placeholder="First name"/>
                <input type="text" class="block outline-none border border-grey-light w-full p-2 rounded mt-3" placeholder="Last name"/>
                <input type="text" class="block outline-none border border-grey-light w-full p-2 rounded mt-3" placeholder="Username"/>
                <input type="password" class="block outline-none border border-grey-light w-full p-2 rounded mt-3" placeholder="Password"/>
                <button class="block bg-transparent border-green-600 border text-green-600 hover:bg-green-600 hover:text-white ease-in-out duration-150 w-full p-2 rounded mt-3">Submit</button>
                <p class="text-center mt-2">Have an account? <a href="#" class="text-blue-600">Sign In</a>!</p>
            </form>
        </div>
    </div>
</template>
<script>
import axios from 'axios'

export default {
    data() {
        return {
            image : '',
            user : {
                username : '',
                password : '',
            }
        }
    },
    methods : {
        createUser() {
            let user = new FormData()
            
            for (let i in this.user) {
                user.append(i, this.user[i])
            }
            
            axios.post('http://127.0.0.1:8000/api/users/', user)
            .then((response) => {
                if (response.status === 201) {
                    axios.post('http://127.0.0.1:8000/api/token/', user)
                    .then((response) => {
                        const jwt_access = response.data.access
                        const jwt_refresh = response.data.refresh
                        this.$cookies.set('jwt_access', jwt_access, '14d')
                        this.$cookies.set('jwt_refresh', jwt_refresh, '30d')
                    })
                }
            })
        }
    },
    beforeMount() {
        axios.get('')
    }
}
</script>
<style lang="">
    
</style>
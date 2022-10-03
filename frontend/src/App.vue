<template lang="">
    <div>
        <div style="margin-bottom:5px;"><input type="text" v-model="user.username"></div>
        <div style="margin-bottom:5px;"><input type="text" v-model="user.password"></div>
        <button @click="createUser()">Create user</button>
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
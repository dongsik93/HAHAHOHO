<template>
    <div>
        <v-container>
            <v-row>
                <v-col cols="12" md="8" offset-md="2">
                    <div>
                        <h1 class="gamjaFont">자유게시판 수정하기</h1>
                    </div>
                    <v-divider></v-divider>
                    <v-form ref="form" v-model="valid">
                        <v-text-field
                        v-model="title"
                        :counter="10"
                        label="글 제목"
                        ></v-text-field>

                        <v-textarea
                        outlined
                        v-model="contents"
                        label="글 내용"
                        ></v-textarea>
                    </v-form>
                    <v-row>
                        <div class="ml-auto pa-2">
                            <v-btn @click="updateFree()" dark color="#74b4a0">
                                수정하기
                            </v-btn>
                        </div>
                    </v-row>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
export default {
    name: 'UpdateFreeboard',
    data () {
        return {
        title: '',
        contents: '',
        valid: true,
        }
    },
    mounted () {
        this.id = this.$route.params.id
        this.getDetail();
    },
    methods: {
        getDetail: function () {
            const baseUrl = this.$store.state.baseUrl
            const apiUrl = baseUrl + 'boards/free/' + this.id 
            this.$http.get(apiUrl)
                .then(res => {
                    this.title = res.data.title
                    this.contents = res.data.contents
                })
                .catch(err => {
                    console.log(err)
                })
        },
        updateFree: function () {
            const baseUrl = this.$store.state.baseUrl
            let form = new FormData()

            form.append('title', this.title)
            form.append('contents', this.contents)
            form.append('user', this.$store.state.user_id)
            form.append('username', this.$store.state.user_name)
            form.append('post', 2) // 2 : 자유 게시판 Default

            const apiUrl = baseUrl + 'boards/free/' + this.id

            // axios.post(baseUrl + 'boards/free', form, {
            //     headers: {
            //     'Authorization': 'Bearer ' + this.$store.state.user_jwt
            //     }
            // })

            this.$http.put(apiUrl, form)
            .then(res => {
                // window.location.href = 'http://localhost:8080/board';
                // this.$EventBus.$emit('boardPage', 1)
                // this.$router.push({path: 'board', porops: {poropsPage: 1}})
                this.$router.go(-1)
            })
            .catch(err => {
                console.log("자유게시판 글작성에 실패하였습니다.")
                console.log(err)
            })
        },
    }
}
</script>
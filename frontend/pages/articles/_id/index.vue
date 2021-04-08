<template>
    <div>
        <h2 class="head">{{article.article_title}}</h2>
        <p v-html="article.article_text"></p>
        <em>{{formatDate(article.pub_date)}}</em>
        <hr>
        <template v-for="c in comment">
          <div :key="c.id">
            <div v-if="article.id==c.article">
              <div class="comment">
                <strong class="mr-2">{{c.author_name}}</strong><em>{{formatDate(c.comm_date)}}</em>
                <p></p>
                <p class="text_comment">{{c.comment_text}}</p>
                <hr>
              </div>
            </div>
          </div>
        </template>
        <form @submit.prevent="submitComment">
          <input type="text" v-model="comm.author_name" class="form-control" placeholder="Ваше имя" name ="name"> <br>
          <textarea   v-model="comm.comment_text" class="form-control"  name="text" cols="145"  required=""  placeholder="Текст комментария" rows="5" style="overflow: hidden; word-wrap: break-word; resize: none; height: 160px; "></textarea><br>
          <button  class="btn btn-outline-primary" type="submit">Отправить</button>
        </form>
    </div>
    
</template>
<script>
export default {
  async asyncData({ $axios, params }) {
    try {
      let article = await $axios.$get(`/articles/${params.id}`);
      let comment = await $axios.$get(`/comment`);
      return { article, comment };

    } catch (e) {
      return { article: [], comment: [] };
    }

  },
  data({ params }) {
    return {
      article: {
      },
      comment:{
      },
      comm:{
            article:  this.$route.params.id,
            author_name: "",
            comment_text: ""
      }
    };
  },
  head() {
    return {
      title:  this.article.article_title,
    };
  },
  methods: {
        async submitComment({ params }) {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.comm) {
        formData.append(data, this.comm[data]);
      }
      try {
        let response = await this.$axios.$post("/comment/", formData, config);
        this.$router.params.id;
      } catch (e) {
        console.log(e);
      }
    },
      formatDate(date) {
      const options = { year: 'numeric', month: 'short', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric'}
      return new Date(date).toLocaleDateString('ru', options)
    }
},
};
</script>
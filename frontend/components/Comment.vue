<!--<template>
<div>
    <template v-for="c in comment">
          <div :key="c.id">
            <div v-if=" article==c.article">
              <div class="comment">
                <strong>{{c.author_name}}</strong><br><em>{{formatDate(c.comm_date)}}</em>
                <p></p>
                <p class="text_comment">{{c.comment_text}}</p>
              </div>
            </div>
            <div v-else></div>
        </div>
        <hr>
        <form @submit.prevent="submitComment" :key="c.id">
        <div v-if="article == c.article">
         <input type="text" v-model="article" class="form-control" placeholder="ID статьи"><br>
          <input type="text" v-model="author_name" class="form-control" placeholder="Ваше имя" name ="name"> <br>
          <textarea   v-model="comment_text" class="form-control"  name="text" cols="145"  required=""  placeholder="Текст комментария" rows="5" style="overflow: hidden; word-wrap: break-word; resize: none; height: 160px; "></textarea><br>
          <button  class="btn btn-outline-primary" type="submit">Отправить</button>
        </div>
        </form>
    </template>

</div>
</template>
<script>
export default {
    name: "Comment",
    props: ["comment", "article"],
    data () {
        return{
            
            article:  null,
            author_name: "",
            comment_text: ""
        }
    },

    methods: {
    async submitComment() {
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in this.data) {
        formData.append(data, this.data[data]);
      }
      try {
        let response = await this.$axios.$post("/comment/", formData, config);
        this.$router.push("thanks");
      } catch (e) {
        console.log(e);
      }
    },
    formatDate(date) {
      const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric'}
      return new Date(date).toLocaleDateString('ru', options)
    }
    }
}
</script>-->
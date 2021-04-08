<template>
 <div>
    <header class="blog-header py-3">
    <div class="row flex-nowrap justify-content-between align-items-center">
      <div class="col-4 pt-1">
        <!--<a class="btn btn-sm btn-outline-secondary" href="http://127.0.0.1:8000/articles/">Назад</a>-->
      </div>
      <div class="col-4 text-center">
        <a class="blog-header-logo text-dark names_logo" href="#">Блог</a>
      </div>
      <div class="col-4 d-flex justify-content-end align-items-center">
      </div>

    </div>
    </header>
     <div class="nav-scroller py-1 mb-2">
    <nav class="names_logo">
      <nuxt-link exact no-prefetch class="p-2 text-muted" to="/">Главная</nuxt-link>
      <nuxt-link class="p-2 text-muted"  to="/articles">Список статей</nuxt-link>
      <nuxt-link class="p-2 text-muted" to="/faq">FAQ</nuxt-link>
    </nav>
  </div>
  <nuxt />
  <footer class="footer">
  <p>©{{new Date().getFullYear() }} Дизайн блога взят из <a href="https://getbootstrap.com/">Bootstrap</a> от <a href="https://twitter.com/mdo">@mdo</a>.</p>
  <p>
    <a href="#">Наверх</a>
  </p></footer>
  </div>
</template>
<script>
export default {
  head() {
    return {
      title: "Список статей"
    };
  },
};
</script>
<style>
@font-face {
  src: url(https://code.s3.yandex.net/web-code/fonts/SuisseIntl-Book.woff);
  font-family: 'Suisse';
  font-weight: normal;
}

@font-face {
  src: url(https://code.s3.yandex.net/web-code/fonts/SuisseIntl-Bold.woff
);
  font-family: 'Suisse';
  font-weight: bold;
 
}


html {
  height: 100%;
  margin: 0;
  -webkit-font-smoothing: antialiased;
}

body {
  background-color:  white;
  color: black;
  width: 80%;
  height: 100%;
  margin: 0 auto;
  font-size: 100%;
  font-family: 'Suisse';
  box-sizing: border-box;
  padding-left: 36px;
  padding-right: 36px;
  max-height: 100vh;
 
}

.footer{
  padding: 2.5rem 0;
  color: #999;
  text-align: center;
  background-color: white;
  border-top: .05rem solid #e5e5e5;
  margin-top: 10px;
    
  }
  .footer-author{
    margin-bottom: 0;
  }
.form {
  margin-top: 8px;
  }
  .name {
font-family: "Playfair Display", Georgia, "Times New Roman", serif;
font-size: 15px;
}
.head {
    margin-top: 3px;
    text-align: center;
    font-family: "Playfair Display", Georgia, "Times New Roman", serif;
    font-size: 25px;
}
.h3{
    font-family: "Playfair Display", Georgia, "Times New Roman", serif;
    
}
.article{
    color: black;
}
.comment{
  font-family: 'Suisse';
  font-size: 15px;
}
.blog-header {
  margin-top: -10px;
  line-height: 1;
  border-bottom: 1px solid #e5e5e5;
}

.blog-header-logo {
  font-family: "Playfair Display", Georgia, "Times New Roman", serif;
  font-size: 50px;
}

.blog-header-logo:hover {
  text-decoration: none;
}
.text_comment {
  margin-top: -13px;
}
.names_logo{
  text-align: center;
  
}
</style>
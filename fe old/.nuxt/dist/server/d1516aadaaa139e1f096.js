exports.ids=[15],exports.modules={245:function(r,t,e){"use strict";var o={props:["text"],methods:{onClose(){this.$emit("dismissed")}}},n=e(1),component=Object(n.a)(o,(function(){var r=this.$createElement;return(this._self._c||r)("v-alert",{attrs:{type:"error",dismissible:"",value:!0},on:{input:this.onClose}},[this._v("\n    "+this._s(this.text)+"\n")])}),[],!1,null,null,"1effbc06");t.a=component.exports},343:function(r,t,e){"use strict";e.r(t);var o={components:{Alert:e(245).a},data(){return{password:"",confirmPassword:"",errors:{password:[],confirmPassword:[]},rules:{required:r=>!!r||"Required.",comparePasswords:r=>r===this.password||"Passwords do not match."}}},computed:{uid(){return this.$route.params.uid},token(){return this.$route.params.token},error(){return this.$store.getters.error},loading(){return this.$store.getters.loading}},watch:{error(r){if(null!==r){console.log(r.response.data);for(let t in r.response.data)"new_password1"===t?this.errors.password=r.response.data[t]:"new_password2"===t?this.errors.confirmPassword=r.response.data[t]:this.errors[t]=r.response.data[t]}}},methods:{onRestorePasswordConfirm(){this.$store.dispatch("restorePasswordConfirm",{uid:this.uid,token:this.token,new_password1:this.password,new_password2:this.confirmPassword})},onDismissed(){this.$store.dispatch("clearError")}}},n=e(1),component=Object(n.a)(o,(function(){var r=this,t=r.$createElement,e=r._self._c||t;return e("v-container",[r.error?e("v-layout",{attrs:{row:""}},[e("v-flex",{attrs:{xs12:"",sm8:"","offset-sm2":""}},r._l(r.errors.token,(function(t){return e("alert",{key:Math.random().toString(10).substr(2,6),attrs:{text:t},on:{dismissed:r.onDismissed}})})),1)],1):r._e(),r._v(" "),e("v-layout",{attrs:{row:""}},[e("v-flex",{attrs:{xs12:"",sm8:"","offset-sm2":""}},[e("v-card",[e("v-card-text",[e("v-container",[e("form",{on:{submit:function(t){return t.preventDefault(),r.onRestorePasswordConfirm(t)}}},[e("v-layout",{attrs:{row:""}},[e("v-flex",{attrs:{"xs-12":""}},[e("v-text-field",{attrs:{name:"password",label:"New password",id:"password",type:"password",rules:[r.rules.required],error:r.errors.password.length>0,"error-messages":r.errors.password},on:{focus:function(t){r.errors.password=[]}},model:{value:r.password,callback:function(t){r.password=t},expression:"password"}})],1)],1),r._v(" "),e("v-layout",{attrs:{row:""}},[e("v-flex",{attrs:{"xs-12":""}},[e("v-text-field",{attrs:{name:"confirmPassword",label:"Confirm new password",id:"confirmPassword",type:"password",rules:[r.rules.required,r.rules.comparePasswords],error:r.errors.confirmPassword.length>0,"error-messages":r.errors.confirmPassword},on:{focus:function(t){r.errors.confirmPassword=[]}},model:{value:r.confirmPassword,callback:function(t){r.confirmPassword=t},expression:"confirmPassword"}})],1)],1),r._v(" "),e("v-layout",{attrs:{row:""}},[e("v-flex",{attrs:{"xs-12":""}},[e("v-btn",{staticClass:"primary",attrs:{type:"submit",disabled:r.loading,loading:r.loading}},[r._v("\n                    Save\n                    "),e("span",{staticClass:"custom-loader",attrs:{slot:"loader"},slot:"loader"},[e("v-icon",{attrs:{light:""}},[r._v("cached")])],1)])],1)],1)],1)])],1)],1)],1)],1)],1)}),[],!1,null,null,"329207c0");t.default=component.exports}};
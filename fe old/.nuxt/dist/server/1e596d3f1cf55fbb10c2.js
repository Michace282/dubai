exports.ids=[13],exports.modules={159:function(t,e,n){var content=n(169);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);var o=n(3).default;t.exports.__inject__=function(t){o("fa589d60",content,!0,t)}},167:function(t,e,n){t.exports=n.p+"img/17a4ca0.png"},168:function(t,e,n){"use strict";n.r(e);var o=n(159),r=n.n(o);for(var d in o)"default"!==d&&function(t){n.d(e,t,(function(){return o[t]}))}(d);e.default=r.a},169:function(t,e,n){(e=n(2)(!1)).push([t.i,".loader[data-v-78e9a330]{width:100%;height:100%;display:-webkit-box;display:flex;-webkit-box-align:start;align-items:flex-start;-webkit-box-pack:center;justify-content:center;z-index:1000;background:#fff}.loader .blick[data-v-78e9a330]{width:30px;height:300px;-webkit-transform:rotate(45deg);transform:rotate(45deg);background:hsla(0,0%,100%,.67843);position:absolute;top:0;-webkit-animation:slide-data-v-78e9a330 2s ease infinite;animation:slide-data-v-78e9a330 2s ease infinite;-webkit-filter:blur(7px);filter:blur(7px)}.loader img[data-v-78e9a330]{margin-top:50px}@-webkit-keyframes slide-data-v-78e9a330{0%{left:0}to{left:1000px}}@keyframes slide-data-v-78e9a330{0%{left:0}to{left:1000px}}",""]),t.exports=e},170:function(t,e,n){"use strict";var o={name:"Loader"},r=n(1);var component=Object(r.a)(o,(function(){var t=this.$createElement;return(this._self._c||t)("div",{staticClass:"loader"},[this._ssrNode('<div class="blick" data-v-78e9a330></div> <img'+this._ssrAttr("src",n(167))+' alt="loader" data-v-78e9a330>')])}),[],!1,(function(t){var e=n(168);e.__inject__&&e.__inject__(t)}),"78e9a330","709e8037");e.a=component.exports},229:function(t,e,n){var content=n(289);"string"==typeof content&&(content=[[t.i,content,""]]),content.locals&&(t.exports=content.locals);var o=n(3).default;t.exports.__inject__=function(t){o("0bc8bcb0",content,!0,t)}},287:function(t,e){var n={kind:"Document",definitions:[{kind:"OperationDefinition",operation:"query",name:{kind:"Name",value:"pageDetail"},variableDefinitions:[{kind:"VariableDefinition",variable:{kind:"Variable",name:{kind:"Name",value:"slug"}},type:{kind:"NamedType",name:{kind:"Name",value:"String"}},directives:[]}],directives:[],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"pageDetail"},arguments:[{kind:"Argument",name:{kind:"Name",value:"slug"},value:{kind:"Variable",name:{kind:"Name",value:"slug"}}}],directives:[],selectionSet:{kind:"SelectionSet",selections:[{kind:"Field",name:{kind:"Name",value:"name"},arguments:[],directives:[]},{kind:"Field",name:{kind:"Name",value:"slug"},arguments:[],directives:[]},{kind:"Field",name:{kind:"Name",value:"text"},arguments:[],directives:[]}]}}]}}],loc:{start:0,end:111}};n.loc.source={body:"query pageDetail($slug: String) {\n    pageDetail(slug: $slug) {\n        name\n        slug\n        text\n    }\n}\n",name:"GraphQL request",locationOffset:{line:1,column:1}};var o={};function r(t,e){for(var i=0;i<t.definitions.length;i++){var element=t.definitions[i];if(element.name&&element.name.value==e)return element}}n.definitions.forEach((function(t){if(t.name){var e=new Set;!function t(e,n){if("FragmentSpread"===e.kind)n.add(e.name.value);else if("VariableDefinition"===e.kind){var o=e.type;"NamedType"===o.kind&&n.add(o.name.value)}e.selectionSet&&e.selectionSet.selections.forEach((function(e){t(e,n)})),e.variableDefinitions&&e.variableDefinitions.forEach((function(e){t(e,n)})),e.definitions&&e.definitions.forEach((function(e){t(e,n)}))}(t,e),o[t.name.value]=e}})),t.exports=n,t.exports.pageDetail=function(t,e){var n={kind:t.kind,definitions:[r(t,e)]};t.hasOwnProperty("loc")&&(n.loc=t.loc);var d=o[e]||new Set,l=new Set,c=new Set;for(d.forEach((function(t){c.add(t)}));c.size>0;){var f=c;c=new Set,f.forEach((function(t){l.has(t)||(l.add(t),(o[t]||new Set).forEach((function(t){c.add(t)})))}))}return l.forEach((function(e){var o=r(t,e);o&&n.definitions.push(o)})),n}(n,"pageDetail")},288:function(t,e,n){"use strict";n.r(e);var o=n(229),r=n.n(o);for(var d in o)"default"!==d&&function(t){n.d(e,t,(function(){return o[t]}))}(d);e.default=r.a},289:function(t,e,n){(e=n(2)(!1)).push([t.i,".text-box[data-v-b103a2fc]{display:block;-webkit-box-pack:justify;justify-content:space-between;margin-top:60px}@media (max-width:991px){.text-box[data-v-b103a2fc]{width:-webkit-fit-content;width:-moz-fit-content;width:fit-content;-webkit-box-orient:vertical;-webkit-box-direction:normal;flex-direction:column;-webkit-box-pack:start;justify-content:flex-start;margin-top:45px}}.text-box .text[data-v-b103a2fc]{max-width:530px;font-family:Inter-Light;font-size:18px;color:#000}@media (max-width:767px){.text-box .text[data-v-b103a2fc]{line-height:22px}}@media (min-width:992px){.text-box .text.mr-60[data-v-b103a2fc]{margin-right:60px}}@media (max-width:991px){.text-box .photo[data-v-b103a2fc]{width:-webkit-fit-content;width:-moz-fit-content;width:fit-content;margin:0 auto 45px}}@media (max-width:450px){.text-box .photo img[data-v-b103a2fc]{width:240px}}@media (min-width:992px){.text-box .photo img[data-v-b103a2fc]{width:100%}}",""]),t.exports=e},351:function(t,e,n){"use strict";n.r(e);var o={components:{Loader:n(170).a},name:"_slug",data:()=>({metaData:null}),head(){return this.metaData},methods:{update(data){if(data.data&&data.data.pageDetail){let content="";"privacy_policy"==data.data.pageDetail.slug&&(content="The DC&S Company Privacy Notice."),"terms_condition"==data.data.pageDetail.slug&&(content="Terms and conditions of online shopping at dcsdubai.com"),this.metaData={title:data.data.pageDetail.name,meta:[{hid:"description",name:"description",content:content}]},this.$store.commit("set_breadcrumbs",[{route:"/",name:"Home"},{route:{name:"page-slug",params:{slug:data.data.pageDetail.slug}},name:data.data.pageDetail.name}])}}}},r=n(1);var component=Object(r.a)(o,(function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("div",{staticClass:"container"},[o("ApolloQuery",{attrs:{query:n(287),variables:{slug:t.$route.params.slug}},on:{result:t.update},scopedSlots:t._u([{key:"default",fn:function(e){var n=e.result,r=n.error,data=n.data;return[e.isLoading||r?o("div",{staticClass:"loading apollo mt-85"},[o("loader")],1):data&&data.pageDetail?o("div",{staticClass:"result apollo"},[o("div",{staticClass:"row"},[o("div",{staticClass:"col-12"},[o("base-title",{staticClass:"mt-30",attrs:{title:data.pageDetail.name}}),t._v(" "),o("div",{staticClass:"text-box",domProps:{innerHTML:t._s(data.pageDetail.text)}})],1)])]):t._e()]}}])})],1)}),[],!1,(function(t){var e=n(288);e.__inject__&&e.__inject__(t)}),"b103a2fc","e450c2cc");e.default=component.exports}};
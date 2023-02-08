<template>
    <div class="modal-container">
        <div class="form-modal">
            <a href.prevent class="exit" @click="$emit('hide')"><img src="~/assets/images/icons/exit.svg" alt="exit" /></a>
            <base-title title="Confirm Reset Password" />
<!--            <socials-auth class="mt-30" />-->
            <div class="input-box">
                <base-input
                    class="mt-30"
                    :class="{ error: $v.code.$error }"
                    label="Code"
                    type="text"
                    v-model="$v.code.$model"
                    name="code"
                />
            </div>
            <div class="text-right mt-30">
                <button class="btn btn-black" @click="Reset">Reset</button>
                <a href.prevent class="link underline mt-15 d-block" @click="$emit('showAuthModal')"
                    >Already have an account? Log in</a
                >
            </div>
        </div>
    </div>
</template>
<script>
    function setCookie(name,value,days) {
      var expires = "";
      if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
      }
      document.cookie = name + "=" + (value || "")  + expires + "; path=/";
    }
    function getCookie(name) {
      var nameEQ = name + "=";
      var ca = document.cookie.split(';');
      for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
      }
      return null;
    }
    function eraseCookie(name) {   
       document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    }
    import BaseInput from '../fields/BaseInput.vue';
    import { required } from 'vuelidate/lib/validators';

    export default {
        name: 'ConfirmForm',
        components: { BaseInput },
        data() {
            return {
                code: ''
            };
        },
        validations: {
            code: {
             required
            }
        },
        created() {
            this.$bvToast.toast('We have sent a security code to your email box. Check it and enter the code here', {
               title: 'Restore Account',
               variant: 'success',
            });
        },
        methods: {
            Reset() {
                let v = this;
                v.$v.$touch();
                if (!v.$v.$error) {
                  let code = getCookie('restore-code')
                  console.log(code)
                  console.log(v.code )
                  if (v.code == code) {
                     v.$nuxt.$emit('show-pass-modal');
                  } else {
                     v.$emit('showResetModal')
                  }  
                }
            },
        },
    };
</script>
<style lang="less" scoped></style>

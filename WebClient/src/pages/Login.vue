<script>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';
import { setCookie } from '../components/utils.js'

export default {
    components: {
        Form,
        Field,
    },
    data() {
        const formSchema = Yup.object().shape({
            email: Yup.string()
                .required('Email is required')
                .email('Email is invalid'),
            password: Yup.string()
                .min(6, 'Password must be at least 6 characters')
                .required('Password is required')
        });
        return {
            formSchema: formSchema
        }
    },
    methods: {
        async onSubmit(values) {
            try {
                const response = await fetch(`${import.meta.env.VITE_APP_API_BASE_ENDPOINT}/v1/auth/signin`, {
                    method: 'POST',
                    mode: 'cors',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        "email": values.email,
                        "password": values.password
                    })
                });
                const result = await response.json();
                if (!response.ok | response.status != 200) {
                    throw { ...result, ...{ 'code': response.status } }
                }

                setCookie("vueadmin-user-access-token", result.token)
                this.$router.push('/dashboard')
            } catch (error) {
                console.error('error in user signin', JSON.stringify(error));
                if (error?.code === 400) {
                    console.log("Error in user input")
                }
                else if (error?.code === 404) {
                    console.log("Url not found")
                } else {
                    console.log("Internal server error")
                }
            }
        }
    }
}

</script>

<template>
    <section class="login-page">
        <div class="login-box">
            <div class="login-card">
                <div class="login-card-header text-center">
                    <p class="login-header-text"><b>Vue</b>Admin</p>
                </div>
                <div class="login-card-body">
                    <p class="login-box-msg">Sign in to start your session</p>
                    <Form @submit="onSubmit" :validation-schema="formSchema" v-slot="{ errors }">
                        <div class="input-container">
                            <div class="input-group mb-3">
                                <Field type="email" name="email" class="form-control" placeholder="Email"
                                    :class="{ 'is-invalid': errors.email }" />
                                <div class="input-group-append">
                                    <div class="input-group-text">
                                        <font-awesome-icon icon="fa-envelope" />
                                    </div>
                                </div>
                            </div>
                            <p class="invalid-feedback">{{ errors.email }}</p>
                        </div>
                        <div class="input-container">
                            <div class="input-group mb-3">
                                <Field type="password" name="password" class=" form-control" placeholder="Password"
                                    :class="{ 'is-invalid': errors.password }" />
                                <div class="input-group-append">
                                    <div class="input-group-text">
                                        <font-awesome-icon icon="fa-lock" />
                                    </div>
                                </div>
                            </div>
                            <p class="invalid-feedback">{{ errors.password }}</p>
                        </div>
                        <div class="login-box-footer">
                            <p class="forgot-password-link">
                                <router-link to="/forgot-password">Forgot my password?</router-link>
                            </p>
                            <div class="login-button">
                                <button type="submit" class="btn-login">Sign In</button>
                            </div>
                        </div>
                    </Form>
                </div>
            </div>
        </div>
    </section>
</template>
<style>
.login-page {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #e9ecef;
}

.login-box {
    width: 360px;
    margin: 0px 10px;
}

.login-card {
    position: relative;
    display: flex;
    flex-direction: column;
    word-wrap: break-word;
    background-color: #ffffff;
    border: 0 solid rgba(0, 0, 0, .125);
    border-radius: 5px;
    border-top: 4px solid #64c5b1;
    box-shadow: 0 0 1px rgba(0, 0, 0, .1), 0 1px 2px rgba(0, 0, 0, .1);
}

.login-card-header {
    background-color: transparent;
    border-bottom: 1px solid rgba(0, 0, 0, .125);
    padding: 1rem 1.25rem;
    position: relative;
}

.login-card-body {
    flex: 1 1 auto;
    padding: 1.25rem;
}

.login-box-msg {
    padding: 0 20px 20px;
    text-align: center;
    margin: 5px 0px;
}

.input-group {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    align-items: stretch;
    width: 100%;
}

.input-container {
    margin-bottom: 1rem !important;
}

.input-container .invalid-feedback {
    font-size: 12px;
    color: red;
}

.form-control {
    position: relative;
    width: 100%;
    height: calc(2.25rem + 2px);
    padding: .375rem .75rem;
    font-size: 1rem;
    font-weight: 400;
    color: #495057;
    font-family: inherit;
    background-color: #fff;
    border: 1px solid #ced4da;
    border-radius: .25rem;
    box-shadow: inset 0 0 0 transparent;
    flex: 1 1 auto;
    width: 1%;
    outline: none;
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
}

.input-group-append {
    margin-left: -1px;
    display: flex;
}

.input-group-text {
    display: flex;
    align-items: center;
    padding: .375rem .75rem;
    font-size: 1rem;
    font-weight: 400;
    color: #495057;
    background-color: #e9ecef;
    border: 1px solid #ced4da;
    border-radius: .25rem;
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
}

.login-box-footer {
    display: flex;
    justify-content: space-between;
    padding: 0.75rem 0rem;
}

.btn-login {
    color: #fff;
    background-color: #64c5b1;
    border-color: #64c5b1;
    cursor: pointer;
    font-weight: 400;
    text-align: center;
    user-select: none;
    border: 1px solid transparent;
    padding: .375rem .75rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: .25rem;
}


.login-header-text {
    font-family: inherit;
    font-weight: 500;
    color: inherit;
    font-size: 2.5rem;
}
</style>
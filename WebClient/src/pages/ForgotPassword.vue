<template>
    <section class="fp-page">
        <div class="fp-box">
            <div class="fp-card">
                <div class="fp-card-header text-center">
                    <p class="fp-header-text"><b>Vue</b>Admin</p>
                </div>
                <div class="fp-card-body">
                    <p class="fp-box-msg">You forgot your password? Here you can easily retrieve a new password.</p>
                    <form method="post">
                        <div class="input-group mb-3">
                            <input type="email" class="form-control" placeholder="Email">
                            <div class="input-group-append">
                                <div class="input-group-text">
                                    <font-awesome-icon icon="fa-envelope" />
                                </div>
                            </div>
                        </div>
                        <div class="fp-box-footer">
                            <p class="login-link">
                                <router-link to="/login">Back to Login</router-link>
                            </p>
                            <div class="fp-button">
                                <button type="submit" class="btn-fp">Send</button>
                            </div>
                        </div>
                    </form>

                </div>
            </div>
        </div>
    </section>
</template>
<style>
.fp-page {
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #e9ecef;
}

.fp-box {
    width: 360px;
    margin: 0px 10px;
}

.fp-card {
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

.fp-card-header {
    background-color: transparent;
    border-bottom: 1px solid rgba(0, 0, 0, .125);
    padding: 1rem 1.25rem;
    position: relative;
}

.fp-card-body {
    flex: 1 1 auto;
    padding: 1.25rem;
}

.fp-box-msg {
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
    margin-bottom: 1rem !important;
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

.fp-box-footer {
    display: flex;
    justify-content: space-between;
    padding: 0.75rem 0rem;
}

.btn-fp {
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


.fp-header-text {
    font-family: inherit;
    font-weight: 500;
    color: inherit;
    font-size: 2.5rem;
}
</style>
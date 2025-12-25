<template>
    <RouterLink :to="{name: 'home'}">Home</RouterLink>
    <form @submit.prevent="handler">
        <label for="email">E-posta</label>
        <input v-model="email" type="email" name="email" id="email" />
        <br>
        <label for="password">Şifre</label>
        <input v-model="password" type="password" name="password" id="password" />
        <br>
        <button type="submit">Giriş Yap</button>
    </form>
</template>

<script setup lang="ts">
import { useAuth } from '@/stores/auth';
import { ref } from 'vue';

// --- Stores ---
const auth = useAuth()

// --- States ---
const email = ref<string>('superuser@email.com')
const password = ref<string>('Gu190582751')

// --- Methods ---
async function handler() {
    await auth.login({
        username: email.value,
        password: password.value
    })
}
</script>
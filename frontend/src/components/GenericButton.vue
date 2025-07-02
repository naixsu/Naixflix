<template>
    <button
        :class="['btn', sizeClass]"
        :disabled="disabled"
    >
        <i
            v-if="icon"
            :class="`mdi mdi-${icon}`"
        />
        <span v-if="label">{{ label }}</span>
        <slot />
    </button>
</template>

<script setup>
    import { computed, defineProps } from 'vue'

    const props = defineProps({
        label: String,
        icon: String,
        size: {
            type: String,
            default: 'medium', // small, medium, large
        },
        disabled: {
            type: Boolean,
            default: false,
        }
    })

    const sizeClass = computed(() => {
        return {
            small: 'btn-small',
            medium: 'btn-medium',
            large: 'btn-large'
        }[props.size]
    })
</script>

<style scoped>
    .btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-weight: 500;
        cursor: pointer;
        border: none;
        transition: background 0.2s ease;
    }

    .btn i {
        font-size: 1.2em;
    }

    /* Sizes */
    .btn-small {
        padding: 0.25rem 0.5rem;
        font-size: 0.8rem;
    }

    .btn-medium {
        font-size: 1rem;
    }

    .btn-large {
        padding: 0.75rem 1.5rem;
        font-size: 1.2rem;
    }
</style>

# Input

## Descrição
Campo de entrada de texto padrão.

## Importação
`import { Input } from "@/components/ui/input"`

## Props Principais
- Aceita todas as props nativas do HTML `<input>` (ex: `type="email"`, `placeholder`, `disabled`).
- `aria-invalid`: Use `aria-invalid="true"` para aplicar bordas vermelhas quando houver erro de validação.

## Exemplo
```tsx
import { Input } from "@/components/ui/input";

export function EmailInput() {
  return <Input type="email" placeholder="seu@email.com" required />;
}
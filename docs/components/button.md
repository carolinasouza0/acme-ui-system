# Button

## Descrição
Componente acionável padrão. Baseado no Radix UI, suporta composição via `asChild`.

## Importação
`import { Button } from "@/components/ui/button"`

## Props
- `variant`: `default` (primário), `outline` (borda), `secondary` (fundo cinza), `ghost` (transparente), `destructive` (vermelho/perigo), `link` (texto sublinhado).
- `size`: `default`, `xs`, `sm`, `lg`, `icon` (quadrado para ícones), `icon-xs`, `icon-sm`, `icon-lg`.
- `asChild`: (boolean) Use quando quiser que o botão repasse seus estilos para um elemento filho (ex: um `<Link>` do Next.js).

## Exemplo
```tsx
import { Button } from "@/components/ui/button";
import { Trash } from "lucide-react";

export function DeleteButton() {
  return (
    <Button variant="destructive" size="sm" className="gap-2">
      <Trash aria-hidden="true" />
      Excluir
    </Button>
  );
}
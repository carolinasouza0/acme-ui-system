# Card

## Descrição
Container flexível para agrupar informações relacionadas. Possui subcomponentes modulares.

## Importação
`import { Card, CardHeader, CardFooter, CardTitle, CardAction, CardDescription, CardContent } from "@/components/ui/card"`

## Estrutura Básica
O `Card` é o wrapper principal e aceita a prop opcional `size="sm"` para um padding reduzido.

## Exemplo Completo
```tsx
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter, CardAction } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export function UserCard() {
  return (
    <Card size="default" className="w-[350px]">
      <CardHeader>
        <CardTitle>Configurações</CardTitle>
        <CardDescription>Gerencie suas preferências.</CardDescription>
        <CardAction>
           <Button variant="ghost" size="icon-sm">...</Button>
        </CardAction>
      </CardHeader>
      <CardContent>
        <p>Conteúdo principal do card vai aqui.</p>
      </CardContent>
      <CardFooter>
        <Button className="w-full">Salvar Alterações</Button>
      </CardFooter>
    </Card>
  );
}
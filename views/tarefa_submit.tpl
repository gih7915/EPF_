% include('layout.tpl')
<h2>Entregar Tarefa</h2>

<p><strong>{{tarefa.titulo}}</strong> — {{tarefa.disciplina or 'Geral'}}</p>
<p>{{tarefa.descricao or ''}}</p>

<form method="post" action="/tarefas/submit/{{tarefa.id}}">
    <input type="hidden" name="aluno_id" value="{{aluno_id}}">
    <label>Conteúdo da entrega</label><br>
    <textarea name="conteudo" rows="6" cols="60"></textarea><br>
    <label>Data de entrega (YYYY-MM-DD)</label><br>
    <input name="entregue_em" type="text"><br>
    <button type="submit">Enviar</button>
</form>

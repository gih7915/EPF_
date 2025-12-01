% rebase('layout', title='Lançar Notas')

<h2>Lançar Notas</h2>
<p>Professor: {{prof.name}}</p>

<form method="post" action="/lancar_notas">
    <label for="disciplina_id">Disciplina:</label>
    <select id="disciplina_id" name="disciplina_id" required>
        <option value="">Selecione uma turma</option>
        % for turma in minhas_turmas:
        <option value="{{turma.id}}">{{turma.codigo}} - {{turma.nome}} (Turma {{turma.turma}})</option>
        % end
    </select><br>
    
    <label for="aluno">Aluno:</label>
    <input type="text" id="aluno" name="aluno" required><br>
    
    <label for="nota">Nota:</label>
    <input type="number" id="nota" name="nota" min="0" max="10" step="0.1" required><br>
    
    <button type="submit">Lançar Nota</button>
</form>

% rebase('layout', title='Matricular em Disciplina', nav_dict=nav_dict)

<div class="form-section" style="max-width: 700px;">
    <h1>🔐 Matrícula em Disciplina</h1>
    <h3>{{disciplina.codigo}} - {{disciplina.nome}}</h3>
    
    <div class="card">
        <div class="card-body">
            <p><strong>Turma:</strong> {{disciplina.turma}}</p>
            <p><strong>Professor:</strong> {{disciplina.docente_id if disciplina.docente_id else 'A definir'}}</p>
            <p><strong>Horário:</strong> {{disciplina.horario}}</p>
            <p><strong>Local:</strong> {{disciplina.local}}</p>
            <p><strong>Vagas Disponíveis:</strong> {{disciplina.vagas_ofertadas - disciplina.vagas_ocupadas}}</p>
        </div>
    </div>
    
    % if erro:
        <div class="warning">
            ⚠️ {{erro}}
        </div>
    % end
    
    <form action="/disciplinas/matricular/{{disciplina.id}}" method="post" class="form-container">
        <input type="hidden" name="aluno_id" value="{{aluno_id}}">
        
        <div class="form-group">
            <p>Confirme sua matrícula nesta disciplina. Não é necessário código.</p>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Confirmar Matrícula</button>
            <button type="button" onclick="window.location.href='/disciplinas?aluno_id={{aluno_id}}'" class="btn-cancel">
                Cancelar
            </button>
        </div>
    </form>
</div>

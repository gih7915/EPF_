% rebase('layout', title='Faltas', nav_dict=nav_dict if 'nav_dict' in locals() else {})

<div class="titulo">
    <h1>Controle de Faltas</h1>
    <p>Verifique suas faltas</p>
</div>

% if aluno:
    <div class="aluno-info" style="background: #ecf0f1; padding: 12px; border-radius:4px; margin-bottom:16px;">
        <p><strong>Aluno:</strong> {{aluno.name}} &nbsp; <strong>Matrícula:</strong> {{aluno.matricula}}</p>
        <p><strong>Total de faltas:</strong> {{total_faltas}}</p>
    </div>

    <form method="get" action="/minhas_faltas" style="margin-bottom:18px;">
        <input type="hidden" name="aluno_id" value="{{aluno.id}}">
        <label for="disciplina_codigo">Filtrar por disciplina:</label>
        <select name="disciplina_codigo" id="disciplina_codigo" style="margin-left:8px;">
            <option value="" selected>-- Todas --</option>
            % for d in (disciplinas_matriculadas or []):
                <option value="{{d.codigo}}" % if disciplina_selecionada and disciplina_selecionada.codigo == d.codigo: selected % end>{{d.codigo}} - {{d.nome}}</option>
            % end
        </select>
        <button class="btn" type="submit" style="margin-left:8px;">Filtrar</button>
    </form>

    % if faltas_entries:
        <table class="table" style="width:100%; border-collapse:collapse;">
            <thead>
                <tr>
                    <th class="table-header">Disciplina</th>
                    <th class="table-header">Total de Faltas</th>
                    <th class="table-header">Datas</th>
                </tr>
            </thead>
            <tbody>
            % for e in faltas_entries:
                <tr>
                    <td style="padding:8px; border-bottom:1px solid #f1f1f1;">{{e['codigo']}} - {{e['nome']}}</td>
                    <td style="padding:8px; border-bottom:1px solid #f1f1f1; text-align:center;">{{e['total']}}</td>
                    <td style="padding:8px; border-bottom:1px solid #f1f1f1;">% if e['datas']: {{', '.join(e['datas'])}} % else: - % end</td>
                </tr>
            % end
            </tbody>
        </table>
    % else:
        <p><em>Nenhuma falta registrada.</em></p>
    % end

% else:
    <p><em>Aluno não informado. Acesse pelo seu dashboard.</em></p>
% end
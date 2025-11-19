% rebase('layout', title='Formulário Professor')

<section class="form-section">
    <h1>{{'Editar Professor' if prof else 'Adicionar Professor'}}</h1>
    
    <form action="{{action}}" method="post" class="form-container">
        <div class="form-group">
            <label for="name">Nome:</label>
            <input type="text" id="name" name="name" required 
                   value="{{prof.name if prof else ''}}">
        </div>
        
        <div class="form-group">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required 
                   value="{{prof.email if prof else ''}}">
        </div>
        
        <div class="form-group">
            <label for="birthdate">Data de Nascimento:</label>
            <input type="date" id="birthdate" name="birthdate" required 
                   value="{{prof.birthdate if prof else ''}}">
        </div>

        <div class="form-group">
            <label for="cargo">Cargo:</label>
            <select id="cargo" name="cargo" required>
                <option value="" disabled selected>Selecione um cargo</option>
                <option value="Professor">Professor(a)</option>
                <option value="Coordenador">Coordenador(a)</option>
                <option value="Diretor">Diretor(a)</option>
            </select>
        </div>
        
        <div class="form-actions">
            <button type="submit" class="btn-submit">Salvar</button>
            <button type="button" onclick="window.location.href='/profs'" class="btn-cancel">
                Voltar
            </button>
        </div>
    </form>
</section>
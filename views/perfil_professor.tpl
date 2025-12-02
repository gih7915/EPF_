% rebase('layout', title='Meu Perfil', nav_dict=nav_dict)

<div class="titulo">
    <h1>Meu Perfil</h1>
    <p>Verifique suas informações</p>
</div>

<div class="card">
    <div class="card-header">
        <div>
            <h3 class="card-title">Minhas Informações</h3>
        </div>
    </div>
    <div class="card-body">
        <p><strong>Nome:</strong> {{prof.name}}
        <button class="open-modal" id="openModal" modal-id="nome">✏️</button></p>
        <p><strong>Email:</strong> {{prof.email}}
        <button class="open-modal" id="openModal" modal-id="email">✏️</button></p>
        <p><strong>Cargo:</strong> {{prof.cargo}}
        <button class="open-modal" id="openModal" modal-id="cargo">✏️</button></p>
        <p><strong>Data de Nascimento:</strong> {{prof.birthdate}}
        <button class="open-modal" id="openModal" modal-id="birthdate">✏️</button></p>
    </div>
</div>

<div class="modal" id="nome">
    <div class="modal-inner">
        <form action="/perfil_professor?prof_id={{prof.id}}" method="post" class="form-container">
            <div class="form-group">
                <label for="name">Nome:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>

<div class="modal" id="email">
    <div class="modal-inner">
        <form action="/perfil_professor?prof_id={{prof.id}}" method="post" class="form-container">
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>

<div class="modal" id="birthdate">
    <div class="modal-inner">
        <form action="/perfil_professor?prof_id={{prof.id}}" method="post" class="form-container">
            <div class="form-group">
                <label for="birthdate">Data de Nascimento:</label>
                <input type="date" id="birthdate" name="birthdate" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>

<div class="modal" id="cargo">
    <div class="modal-inner">
        <form action="/perfil_professor?prof_id={{prof.id}}" method="post" class="form-container">
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
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>
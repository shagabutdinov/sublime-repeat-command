
def index
  sort_init 'login', 'asc'
  sort_update %w(login firstname lastname mail admin created_on last_login_on)

  # Done!

  @status = params[:status] || 1

  # Done!
  # scope = User.logged.status(@status)
  # scope = scope.like(params[:name]) if params[:name].present?
  # scope = scope.in_group(params[:group_id]) if params[:group_id].present?
  # scope = _process_scope(scope)
  # scope = _process_processed_scope(scope)

  respond_to do |format|
    format.html {
      @groups = Group.all.sort
      render :layout => !request.xhr?
    }
    format.api
  end
end
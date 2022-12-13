package com.example.sqllite14_11_22.adapter

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.RecyclerView
import com.example.sqllite14_11_22.R
import com.example.sqllite14_11_22.models.Usuarios

class UsuariosAdapter(
    private
    val lista: MutableList<Usuarios>,
    private val onItemDelete: (Int) -> Unit,
    private val onItemUpdate: (Usuarios) -> Unit
) : RecyclerView.Adapter<UsuariosViewHolder>() {
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UsuariosViewHolder {
        val v = LayoutInflater.from(parent.context).inflate(R.layout.usuarios_layout, parent, false)
        return UsuariosViewHolder(v)
    }

    override fun onBindViewHolder(holder: UsuariosViewHolder, position: Int) {
        holder.render(lista[position], onItemDelete, onItemUpdate)
    }

    override fun getItemCount() = lista.size
}
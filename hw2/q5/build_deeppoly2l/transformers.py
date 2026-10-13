import torch
from constraintflow.lib.polyexp import PolyExpSparse
from constraintflow.lib.symexp import *
from constraintflow.gbcsr.sparse_tensor import SparseTensor
from constraintflow.lib.llist import Llist
from constraintflow.gbcsr.tensor_ops import *
class deeppoly2l:
	def Affine(self, abs_elem, prev, curr, poly_size, curr_size, prev_size, input_size, batch_size):
		cse_var_33 = prev.dot(curr.get_metadata('weight', batch_size), abs_elem.get_poly_size())
		cse_var_32 = curr.get_metadata('bias', batch_size)
		cse_var_93 = cse_var_33.get_mat(abs_elem)
		cse_var_61 = PolyExpSparse(abs_elem.network, cse_var_93 , binary(cse_var_33.get_const(), cse_var_32, operator.add))
		cse_var_155 = binary(get_dims(cse_var_93), 1, operator.sub)
		vertices_stop1 = False
		cse_var_23 = SparseTensor([], [], 0, torch.tensor([]), dense_const=0.0, type= type(0.0)).unsqueeze(0).unsqueeze(1).unsqueeze(2).repeat(torch.tensor([batch_size, curr_size, poly_size]))
		cse_var_160 = unary(Llist(abs_elem.network, [1]*(cse_var_155), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist()).get_metadata('layer', batch_size), operator.neg)
		cse_var_159 = Llist(abs_elem.network, [1]*(cse_var_155), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_161 = abs_elem.get_elem('L', cse_var_159)
		cse_var_162 = abs_elem.get_elem('U', cse_var_159)
		cse_var_166 = cse_var_162.get_const()
		cse_var_165 = cse_var_162.get_mat(abs_elem)
		cse_var_164 = cse_var_161.get_const()
		cse_var_163 = cse_var_161.get_mat(abs_elem)
		phi_trav_exp1_1_1 = cse_var_61
		while(True):
			cse_var_34 = phi_trav_exp1_1_1.get_mat(abs_elem)
			vertices1_1_1 = binary(cse_var_34, cse_var_23, operator.ne)
			vertices_stop_default1 = get_default_stop([batch_size, curr_size, poly_size], abs_elem, batch_size, curr_size, poly_size)
			vertices_stop_temp1 = binary(SparseTensor([], [], 0, torch.tensor([]), dense_const=vertices_stop1, type= type(vertices_stop1)).unsqueeze(0).unsqueeze(1).unsqueeze(2).repeat(torch.tensor([batch_size, curr_size, poly_size])), vertices_stop_default1, operator.or_)
			vertices1_1_2 = binary(vertices1_1_1, unary(vertices_stop_temp1, operator.not_), operator.and_)
			if(unary(any(vertices1_1_2), operator.not_)):
				break
			priority_vertices1 = get_max_priority(cse_var_160, vertices1_1_2)
			vertices_final_stop1 = binary(vertices_stop_temp1, repeat(unary(priority_vertices1, operator.not_), torch.tensor([batch_size, curr_size, 1])), operator.or_)
			polyexp_stop1 = filter_trav_exp_stop(phi_trav_exp1_1_1, vertices_final_stop1)
			polyexp_not_stop1 = filter_trav_exp_not_stop(phi_trav_exp1_1_1, vertices_final_stop1)
			cse_var_147 = polyexp_not_stop1.get_mat(abs_elem)
			cse_var_144 = cse_var_147.unsqueeze(3)
			cse_var_139 = clamp(cse_var_147, False, 0)
			cse_var_141 = clamp(cse_var_147, True, 0)
			cse_var_135 = clamp(cse_var_144, False, 0)
			cse_var_137 = clamp(cse_var_144, True, 0)
			cse_var_85 = binary(inner_prod(cse_var_141, cse_var_164.squeeze(1)), inner_prod(cse_var_139, cse_var_166.squeeze(1)), operator.add)
			cse_var_86 = binary(inner_prod(cse_var_137.squeeze(3), cse_var_163.squeeze(1)), inner_prod(cse_var_135.squeeze(3), cse_var_165.squeeze(1)), operator.add)
			cse_var_84 = binary(cse_var_85, polyexp_not_stop1.get_const(), operator.add)
			trav_exp1_4_3 = PolyExpSparse(abs_elem.network, binary(cse_var_86, polyexp_stop1.get_mat(abs_elem), operator.add) , binary(cse_var_84, polyexp_stop1.get_const(), operator.add))
			phi_trav_exp1_1_1 = trav_exp1_4_3
		vertices_stop2 = False
		var_7 = abs_elem.get_elem('La', cse_var_159)
		cse_var_124 = var_7.get_const()
		cse_var_120 = var_7.get_mat(abs_elem)
		phi_trav_exp2_5_1 = cse_var_61
		while(True):
			cse_var_24 = phi_trav_exp2_5_1.get_mat(abs_elem)
			vertices2_5_1 = binary(cse_var_24, cse_var_23, operator.ne)
			vertices_stop_default2 = get_default_stop([batch_size, curr_size, poly_size], abs_elem, batch_size, curr_size, poly_size)
			vertices_stop_temp2 = binary(SparseTensor([], [], 0, torch.tensor([]), dense_const=vertices_stop2, type= type(vertices_stop2)).unsqueeze(0).unsqueeze(1).unsqueeze(2).repeat(torch.tensor([batch_size, curr_size, poly_size])), vertices_stop_default2, operator.or_)
			vertices2_5_2 = binary(vertices2_5_1, unary(vertices_stop_temp2, operator.not_), operator.and_)
			if(unary(any(vertices2_5_2), operator.not_)):
				break
			priority_vertices2 = get_max_priority(cse_var_160, vertices2_5_2)
			vertices_final_stop2 = binary(vertices_stop_temp2, repeat(unary(priority_vertices2, operator.not_), torch.tensor([batch_size, curr_size, 1])), operator.or_)
			polyexp_stop2 = filter_trav_exp_stop(phi_trav_exp2_5_1, vertices_final_stop2)
			polyexp_not_stop2 = filter_trav_exp_not_stop(phi_trav_exp2_5_1, vertices_final_stop2)
			cse_var_131 = polyexp_not_stop2.get_mat(abs_elem)
			cse_var_128 = cse_var_131.unsqueeze(3)
			cse_var_123 = clamp(cse_var_131, False, 0)
			cse_var_125 = clamp(cse_var_131, True, 0)
			cse_var_119 = clamp(cse_var_128, False, 0)
			cse_var_121 = clamp(cse_var_128, True, 0)
			cse_var_76 = binary(inner_prod(cse_var_125, cse_var_124.squeeze(1)), inner_prod(cse_var_123, cse_var_166.squeeze(1)), operator.add)
			cse_var_77 = binary(inner_prod(cse_var_121.squeeze(3), cse_var_120.squeeze(1)), inner_prod(cse_var_119.squeeze(3), cse_var_165.squeeze(1)), operator.add)
			cse_var_75 = binary(cse_var_76, polyexp_not_stop2.get_const(), operator.add)
			trav_exp2_8_3 = PolyExpSparse(abs_elem.network, binary(cse_var_77, polyexp_stop2.get_mat(abs_elem), operator.add) , binary(cse_var_75, polyexp_stop2.get_const(), operator.add))
			phi_trav_exp2_5_1 = trav_exp2_8_3
		cse_var_18 = Llist(abs_elem.network, [1]*(phi_trav_exp2_5_1.mat.dims-1), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_132 = phi_trav_exp2_5_1.get_mat(abs_elem)
		cse_var_20 = Llist(abs_elem.network, [1]*(phi_trav_exp1_1_1.mat.dims-1), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_133 = phi_trav_exp1_1_1.get_mat(abs_elem)
		l_new = cf_max(binary(binary(inner_prod(clamp(cse_var_133, True, 0), abs_elem.get_elem('l', cse_var_20).squeeze(1)), inner_prod(clamp(cse_var_133, False, 0), abs_elem.get_elem('u', cse_var_20).squeeze(1)), operator.add), phi_trav_exp1_1_1.get_const(), operator.add), binary(binary(inner_prod(clamp(cse_var_132, True, 0), abs_elem.get_elem('l', cse_var_18).squeeze(1)), inner_prod(clamp(cse_var_132, False, 0), abs_elem.get_elem('u', cse_var_18).squeeze(1)), operator.add), phi_trav_exp2_5_1.get_const(), operator.add))
		vertices_stop3 = False
		phi_trav_exp3_9_1 = cse_var_61
		while(True):
			cse_var_10 = phi_trav_exp3_9_1.get_mat(abs_elem)
			vertices3_9_1 = binary(cse_var_10, cse_var_23, operator.ne)
			vertices_stop_default3 = get_default_stop([batch_size, curr_size, poly_size], abs_elem, batch_size, curr_size, poly_size)
			vertices_stop_temp3 = binary(SparseTensor([], [], 0, torch.tensor([]), dense_const=vertices_stop3, type= type(vertices_stop3)).unsqueeze(0).unsqueeze(1).unsqueeze(2).repeat(torch.tensor([batch_size, curr_size, poly_size])), vertices_stop_default3, operator.or_)
			vertices3_9_2 = binary(vertices3_9_1, unary(vertices_stop_temp3, operator.not_), operator.and_)
			if(unary(any(vertices3_9_2), operator.not_)):
				break
			priority_vertices3 = get_max_priority(cse_var_160, vertices3_9_2)
			vertices_final_stop3 = binary(vertices_stop_temp3, repeat(unary(priority_vertices3, operator.not_), torch.tensor([batch_size, curr_size, 1])), operator.or_)
			polyexp_stop3 = filter_trav_exp_stop(phi_trav_exp3_9_1, vertices_final_stop3)
			polyexp_not_stop3 = filter_trav_exp_not_stop(phi_trav_exp3_9_1, vertices_final_stop3)
			cse_var_116 = polyexp_not_stop3.get_mat(abs_elem)
			cse_var_113 = cse_var_116.unsqueeze(3)
			cse_var_108 = clamp(cse_var_116, False, 0)
			cse_var_110 = clamp(cse_var_116, True, 0)
			cse_var_104 = clamp(cse_var_113, False, 0)
			cse_var_106 = clamp(cse_var_113, True, 0)
			cse_var_67 = binary(inner_prod(cse_var_110, cse_var_166.squeeze(1)), inner_prod(cse_var_108, cse_var_164.squeeze(1)), operator.add)
			cse_var_68 = binary(inner_prod(cse_var_106.squeeze(3), cse_var_165.squeeze(1)), inner_prod(cse_var_104.squeeze(3), cse_var_163.squeeze(1)), operator.add)
			cse_var_66 = binary(cse_var_67, polyexp_not_stop3.get_const(), operator.add)
			trav_exp3_12_3 = PolyExpSparse(abs_elem.network, binary(cse_var_68, polyexp_stop3.get_mat(abs_elem), operator.add) , binary(cse_var_66, polyexp_stop3.get_const(), operator.add))
			phi_trav_exp3_9_1 = trav_exp3_12_3
		cse_var_8 = Llist(abs_elem.network, [1]*(phi_trav_exp3_9_1.mat.dims-1), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_117 = phi_trav_exp3_9_1.get_mat(abs_elem)
		u_new = binary(binary(inner_prod(clamp(cse_var_117, True, 0), abs_elem.get_elem('u', cse_var_8).squeeze(1)), inner_prod(clamp(cse_var_117, False, 0), abs_elem.get_elem('l', cse_var_8).squeeze(1)), operator.add), phi_trav_exp3_9_1.get_const(), operator.add)
		return l_new, u_new, cse_var_61, cse_var_61, cse_var_61
	
	def Relu(self, abs_elem, prev, curr, poly_size, curr_size, prev_size, input_size, batch_size):
		cse_var_57 = abs_elem.get_elem('l', prev)
		cse_var_58 = SparseTensor([], [], 0, torch.tensor([]), dense_const=0.0, type= type(0.0)).unsqueeze(0).unsqueeze(1).repeat(torch.tensor([batch_size, curr_size]))
		cse_var_63 = binary(cse_var_57, cse_var_58, operator.ge)
		cse_var_148 = convert_to_float(cse_var_63)
		cse_var_154 = SparseTensor([], [], 0, torch.tensor([]), dense_const=1.0, type= type(1.0)).unsqueeze(0).unsqueeze(1).repeat(torch.tensor([batch_size, curr_size]))
		cse_var_156 = binary(cse_var_154, cse_var_148, operator.sub)
		l_new = binary(binary(cse_var_148, cse_var_57, operator.mul), binary(cse_var_156, cse_var_58, operator.mul), operator.add)
		cse_var_56 = abs_elem.get_elem('u', prev)
		rewrite_new_1 = convert_to_float(binary(cse_var_56, cse_var_58, operator.ge))
		u_new = binary(binary(rewrite_new_1, cse_var_56, operator.mul), binary(binary(cse_var_154, rewrite_new_1, operator.sub), cse_var_58, operator.mul), operator.add)
		cse_var_53 = PolyExpSparse(abs_elem.network, 0.0, 0.0)
		cse_var_38 = SparseTensor([], [], 0, torch.tensor([]), dense_const=cse_var_53.get_const(), type= type(cse_var_53.get_const())).unsqueeze(0).unsqueeze(1).repeat(torch.tensor([batch_size, curr_size]))
		cse_var_39 = cse_var_53.get_mat(abs_elem)
		cse_var_55 = binary(binary(cse_var_57, cse_var_56, operator.add), cse_var_58, operator.ge)
		cse_var_54 = prev.convert_to_poly(abs_elem)
		cse_var_64 = repeat(cse_var_54.get_const(), torch.tensor([batch_size, 1]))
		cse_var_65 = repeat(cse_var_54.get_mat(abs_elem), torch.tensor([batch_size, 1, 1]))
		cse_var_153 = convert_to_float(cse_var_55)
		cse_var_152 = repeat(cse_var_153.unsqueeze(2), torch.tensor([1, 1, poly_size]))
		cse_var_158 = binary(cse_var_154, cse_var_153, operator.sub)
		cse_var_151 = SparseTensor([], [], 0, torch.tensor([]), dense_const=cse_var_39, type= type(cse_var_39)).unsqueeze(0).unsqueeze(1).repeat(torch.tensor([batch_size, curr_size]))
		L_new = PolyExpSparse(abs_elem.network, binary(binary(cse_var_152, cse_var_65, operator.mul), repeat(binary(cse_var_158, cse_var_151, operator.mul).unsqueeze(2), torch.tensor([1, 1, poly_size])), operator.add) , binary(binary(cse_var_153, cse_var_64, operator.mul), binary(cse_var_158, cse_var_38, operator.mul), operator.add))
		cse_var_50 = binary(cse_var_56, cse_var_57, operator.sub)
		cse_var_52 = binary(cse_var_56, cse_var_50, operator.truediv)
		cse_var_101 = binary(cse_var_52, cse_var_64, operator.mul)
		cse_var_102 = binary(repeat(cse_var_52.unsqueeze(2), torch.tensor([1, 1, poly_size])), cse_var_65, operator.mul)
		cse_var_48 = PolyExpSparse(abs_elem.network, 0.0, cse_var_58)
		cse_var_37 = cse_var_48.get_const()
		cse_var_41 = cse_var_48.get_mat(abs_elem)
		cse_var_49 = binary(cse_var_56, cse_var_58, operator.le)
		cse_var_42 = repeat(cse_var_49.unsqueeze(2), torch.tensor([1, 1, poly_size]))
		cse_var_43 = repeat(cse_var_63.unsqueeze(2), torch.tensor([1, 1, poly_size]))
		cse_var_100 = binary(cse_var_101, binary(binary(cse_var_56, cse_var_57, operator.mul), cse_var_50, operator.truediv), operator.sub)
		cse_var_98 = where(cse_var_49, cse_var_37, cse_var_100)
		cse_var_99 = where(cse_var_42, cse_var_41, cse_var_102)
		U_new = PolyExpSparse(abs_elem.network, where(cse_var_43, cse_var_65, cse_var_99) , where(cse_var_63, cse_var_64, cse_var_98))
		cse_var_96 = binary(binary(cse_var_153, cse_var_38, operator.mul), binary(cse_var_158, cse_var_64, operator.mul), operator.add)
		cse_var_97 = binary(repeat(binary(cse_var_153, cse_var_151, operator.mul).unsqueeze(2), torch.tensor([1, 1, poly_size])), binary(repeat(cse_var_158.unsqueeze(2), torch.tensor([1, 1, poly_size])), cse_var_65, operator.mul), operator.add)
		cse_var_149 = convert_to_float(cse_var_49)
		cse_var_157 = binary(cse_var_154, cse_var_149, operator.sub)
		cse_var_94 = binary(binary(cse_var_149, cse_var_37, operator.mul), binary(cse_var_157, cse_var_96, operator.mul), operator.add)
		rewrite_new_7 = repeat(cse_var_149.unsqueeze(2), torch.tensor([1, 1, poly_size]))
		cse_var_95 = binary(binary(rewrite_new_7, cse_var_41, operator.mul), binary(repeat(cse_var_157.unsqueeze(2), torch.tensor([1, 1, poly_size])), cse_var_97, operator.mul), operator.add)
		rewrite_new_8 = repeat(cse_var_148.unsqueeze(2), torch.tensor([1, 1, poly_size]))
		La_new = PolyExpSparse(abs_elem.network, binary(binary(rewrite_new_8, cse_var_65, operator.mul), binary(repeat(cse_var_156.unsqueeze(2), torch.tensor([1, 1, poly_size])), cse_var_95, operator.mul), operator.add) , binary(binary(cse_var_148, cse_var_64, operator.mul), binary(cse_var_156, cse_var_94, operator.mul), operator.add))
		return l_new, u_new, L_new, U_new, La_new
	

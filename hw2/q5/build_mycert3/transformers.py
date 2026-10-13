import torch
from constraintflow.lib.polyexp import PolyExpSparse
from constraintflow.lib.symexp import *
from constraintflow.gbcsr.sparse_tensor import SparseTensor
from constraintflow.lib.llist import Llist
from constraintflow.gbcsr.tensor_ops import *
class mycert3:
	def Affine(self, abs_elem, prev, curr, poly_size, curr_size, prev_size, input_size, batch_size):
		cse_var_27 = prev.dot(curr.get_metadata('weight', batch_size), abs_elem.get_poly_size())
		cse_var_26 = curr.get_metadata('bias', batch_size)
		cse_var_70 = binary(cse_var_27.get_const(), cse_var_26, operator.add)
		cse_var_71 = cse_var_27.get_mat(abs_elem)
		cse_var_45 = PolyExpSparse(abs_elem.network, cse_var_71 , cse_var_70)
		cse_var_113 = binary(get_dims(cse_var_71), 1, operator.sub)
		vertices_stop1 = False
		cse_var_12 = SparseTensor([], [], 0, torch.tensor([]), dense_const=0.0, type= type(0.0)).unsqueeze(0).unsqueeze(1).unsqueeze(2).repeat(torch.tensor([batch_size, curr_size, poly_size]))
		cse_var_116 = unary(Llist(abs_elem.network, [1]*(cse_var_113), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist()).get_metadata('layer', batch_size), operator.neg)
		cse_var_115 = Llist(abs_elem.network, [1]*(cse_var_113), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_117 = abs_elem.get_elem('L', cse_var_115)
		cse_var_118 = abs_elem.get_elem('U', cse_var_115)
		cse_var_120 = cse_var_118.get_const()
		cse_var_119 = cse_var_118.get_mat(abs_elem)
		cse_var_122 = cse_var_117.get_const()
		cse_var_121 = cse_var_117.get_mat(abs_elem)
		phi_trav_exp1_1_1 = cse_var_45
		while(True):
			cse_var_28 = phi_trav_exp1_1_1.get_mat(abs_elem)
			vertices1_1_1 = binary(cse_var_28, cse_var_12, operator.ne)
			vertices_stop_default1 = get_default_stop([batch_size, curr_size, poly_size], abs_elem, batch_size, curr_size, poly_size)
			vertices_stop_temp1 = binary(SparseTensor([], [], 0, torch.tensor([]), dense_const=vertices_stop1, type= type(vertices_stop1)).unsqueeze(0).unsqueeze(1).unsqueeze(2).repeat(torch.tensor([batch_size, curr_size, poly_size])), vertices_stop_default1, operator.or_)
			vertices1_1_2 = binary(vertices1_1_1, unary(vertices_stop_temp1, operator.not_), operator.and_)
			if(unary(any(vertices1_1_2), operator.not_)):
				break
			priority_vertices1 = get_max_priority(cse_var_116, vertices1_1_2)
			vertices_final_stop1 = binary(vertices_stop_temp1, repeat(unary(priority_vertices1, operator.not_), torch.tensor([batch_size, curr_size, 1])), operator.or_)
			polyexp_stop1 = filter_trav_exp_stop(phi_trav_exp1_1_1, vertices_final_stop1)
			polyexp_not_stop1 = filter_trav_exp_not_stop(phi_trav_exp1_1_1, vertices_final_stop1)
			cse_var_107 = polyexp_not_stop1.get_mat(abs_elem)
			cse_var_104 = cse_var_107.unsqueeze(3)
			cse_var_99 = clamp(cse_var_107, False, 0)
			cse_var_101 = clamp(cse_var_107, True, 0)
			cse_var_95 = clamp(cse_var_104, False, 0)
			cse_var_97 = clamp(cse_var_104, True, 0)
			cse_var_62 = binary(inner_prod(cse_var_101, cse_var_122.squeeze(1)), inner_prod(cse_var_99, cse_var_120.squeeze(1)), operator.add)
			cse_var_63 = binary(inner_prod(cse_var_97.squeeze(3), cse_var_121.squeeze(1)), inner_prod(cse_var_95.squeeze(3), cse_var_119.squeeze(1)), operator.add)
			cse_var_61 = binary(cse_var_62, polyexp_not_stop1.get_const(), operator.add)
			trav_exp1_4_3 = PolyExpSparse(abs_elem.network, binary(cse_var_63, polyexp_stop1.get_mat(abs_elem), operator.add) , binary(cse_var_61, polyexp_stop1.get_const(), operator.add))
			phi_trav_exp1_1_1 = trav_exp1_4_3
		cse_var_60 = Llist(abs_elem.network, [1]*(cse_var_45.mat.dims-1), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_59 = cse_var_45.get_mat(abs_elem)
		cse_var_24 = Llist(abs_elem.network, [1]*(phi_trav_exp1_1_1.mat.dims-1), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_108 = phi_trav_exp1_1_1.get_mat(abs_elem)
		cse_var_91 = clamp(cse_var_59, False, 0)
		cse_var_92 = clamp(cse_var_59, True, 0)
		cse_var_111 = abs_elem.get_elem('l', cse_var_60).squeeze(1)
		cse_var_112 = abs_elem.get_elem('u', cse_var_60).squeeze(1)
		l_new = cf_max(binary(binary(inner_prod(clamp(cse_var_108, True, 0), abs_elem.get_elem('l', cse_var_24).squeeze(1)), inner_prod(clamp(cse_var_108, False, 0), abs_elem.get_elem('u', cse_var_24).squeeze(1)), operator.add), phi_trav_exp1_1_1.get_const(), operator.add), binary(binary(inner_prod(cse_var_92, cse_var_111), inner_prod(cse_var_91, cse_var_112), operator.add), cse_var_70, operator.add))
		vertices_stop2 = False
		phi_trav_exp2_5_1 = cse_var_45
		while(True):
			cse_var_13 = phi_trav_exp2_5_1.get_mat(abs_elem)
			vertices2_5_1 = binary(cse_var_13, cse_var_12, operator.ne)
			vertices_stop_default2 = get_default_stop([batch_size, curr_size, poly_size], abs_elem, batch_size, curr_size, poly_size)
			vertices_stop_temp2 = binary(SparseTensor([], [], 0, torch.tensor([]), dense_const=vertices_stop2, type= type(vertices_stop2)).unsqueeze(0).unsqueeze(1).unsqueeze(2).repeat(torch.tensor([batch_size, curr_size, poly_size])), vertices_stop_default2, operator.or_)
			vertices2_5_2 = binary(vertices2_5_1, unary(vertices_stop_temp2, operator.not_), operator.and_)
			if(unary(any(vertices2_5_2), operator.not_)):
				break
			priority_vertices2 = get_max_priority(cse_var_116, vertices2_5_2)
			vertices_final_stop2 = binary(vertices_stop_temp2, repeat(unary(priority_vertices2, operator.not_), torch.tensor([batch_size, curr_size, 1])), operator.or_)
			polyexp_stop2 = filter_trav_exp_stop(phi_trav_exp2_5_1, vertices_final_stop2)
			polyexp_not_stop2 = filter_trav_exp_not_stop(phi_trav_exp2_5_1, vertices_final_stop2)
			cse_var_90 = polyexp_not_stop2.get_mat(abs_elem)
			cse_var_87 = cse_var_90.unsqueeze(3)
			cse_var_82 = clamp(cse_var_90, False, 0)
			cse_var_84 = clamp(cse_var_90, True, 0)
			cse_var_78 = clamp(cse_var_87, False, 0)
			cse_var_80 = clamp(cse_var_87, True, 0)
			cse_var_51 = binary(inner_prod(cse_var_84, cse_var_120.squeeze(1)), inner_prod(cse_var_82, cse_var_122.squeeze(1)), operator.add)
			cse_var_52 = binary(inner_prod(cse_var_80.squeeze(3), cse_var_119.squeeze(1)), inner_prod(cse_var_78.squeeze(3), cse_var_121.squeeze(1)), operator.add)
			cse_var_50 = binary(cse_var_51, polyexp_not_stop2.get_const(), operator.add)
			trav_exp2_8_3 = PolyExpSparse(abs_elem.network, binary(cse_var_52, polyexp_stop2.get_mat(abs_elem), operator.add) , binary(cse_var_50, polyexp_stop2.get_const(), operator.add))
			phi_trav_exp2_5_1 = trav_exp2_8_3
		cse_var_10 = Llist(abs_elem.network, [1]*(phi_trav_exp2_5_1.mat.dims-1), None, None,torch.nonzero(abs_elem.d['llist']).flatten().tolist())
		cse_var_93 = phi_trav_exp2_5_1.get_mat(abs_elem)
		u_new = cf_min(binary(binary(inner_prod(clamp(cse_var_93, True, 0), abs_elem.get_elem('u', cse_var_10).squeeze(1)), inner_prod(clamp(cse_var_93, False, 0), abs_elem.get_elem('l', cse_var_10).squeeze(1)), operator.add), phi_trav_exp2_5_1.get_const(), operator.add), binary(binary(inner_prod(cse_var_92, cse_var_112), inner_prod(cse_var_91, cse_var_111), operator.add), cse_var_70, operator.add))
		return l_new, u_new, cse_var_45, cse_var_45
	
	def Relu(self, abs_elem, prev, curr, poly_size, curr_size, prev_size, input_size, batch_size):
		cse_var_42 = abs_elem.get_elem('l', prev)
		cse_var_43 = SparseTensor([], [], 0, torch.tensor([]), dense_const=0.0, type= type(0.0)).unsqueeze(0).unsqueeze(1).repeat(torch.tensor([batch_size, curr_size]))
		cse_var_47 = binary(cse_var_42, cse_var_43, operator.ge)
		rewrite_new_0 = convert_to_float(cse_var_47)
		cse_var_110 = SparseTensor([], [], 0, torch.tensor([]), dense_const=1.0, type= type(1.0)).unsqueeze(0).unsqueeze(1).repeat(torch.tensor([batch_size, curr_size]))
		l_new = binary(binary(rewrite_new_0, cse_var_42, operator.mul), binary(binary(cse_var_110, rewrite_new_0, operator.sub), cse_var_43, operator.mul), operator.add)
		cse_var_41 = abs_elem.get_elem('u', prev)
		rewrite_new_1 = convert_to_float(binary(cse_var_41, cse_var_43, operator.ge))
		u_new = binary(binary(rewrite_new_1, cse_var_41, operator.mul), binary(binary(cse_var_110, rewrite_new_1, operator.sub), cse_var_43, operator.mul), operator.add)
		cse_var_39 = prev.convert_to_poly(abs_elem)
		cse_var_48 = repeat(cse_var_39.get_const(), torch.tensor([batch_size, 1]))
		cse_var_49 = repeat(cse_var_39.get_mat(abs_elem), torch.tensor([batch_size, 1, 1]))
		cse_var_38 = PolyExpSparse(abs_elem.network, 0.0, 0.0)
		cse_var_40 = binary(binary(cse_var_42, cse_var_41, operator.add), cse_var_43, operator.ge)
		cse_var_109 = convert_to_float(cse_var_40)
		rewrite_new_2 = repeat(cse_var_109.unsqueeze(2), torch.tensor([1, 1, poly_size]))
		cse_var_114 = binary(cse_var_110, cse_var_109, operator.sub)
		L_new = PolyExpSparse(abs_elem.network, binary(binary(rewrite_new_2, cse_var_49, operator.mul), repeat(binary(cse_var_114, SparseTensor([], [], 0, torch.tensor([]), dense_const=cse_var_38.get_mat(abs_elem), type= type(cse_var_38.get_mat(abs_elem))).unsqueeze(0).unsqueeze(1).repeat(torch.tensor([batch_size, curr_size])), operator.mul).unsqueeze(2), torch.tensor([1, 1, poly_size])), operator.add) , binary(binary(cse_var_109, cse_var_48, operator.mul), binary(cse_var_114, SparseTensor([], [], 0, torch.tensor([]), dense_const=cse_var_38.get_const(), type= type(cse_var_38.get_const())).unsqueeze(0).unsqueeze(1).repeat(torch.tensor([batch_size, curr_size])), operator.mul), operator.add))
		cse_var_35 = binary(cse_var_41, cse_var_42, operator.sub)
		cse_var_37 = binary(cse_var_41, cse_var_35, operator.truediv)
		cse_var_75 = binary(cse_var_37, cse_var_48, operator.mul)
		cse_var_76 = binary(repeat(cse_var_37.unsqueeze(2), torch.tensor([1, 1, poly_size])), cse_var_49, operator.mul)
		cse_var_74 = binary(cse_var_75, binary(binary(cse_var_41, cse_var_42, operator.mul), cse_var_35, operator.truediv), operator.sub)
		cse_var_33 = PolyExpSparse(abs_elem.network, 0.0, cse_var_43)
		cse_var_34 = binary(cse_var_41, cse_var_43, operator.le)
		cse_var_72 = where(cse_var_34, cse_var_33.get_const(), cse_var_74)
		cse_var_73 = where(repeat(cse_var_34.unsqueeze(2), torch.tensor([1, 1, poly_size])), cse_var_33.get_mat(abs_elem), cse_var_76)
		U_new = PolyExpSparse(abs_elem.network, where(repeat(cse_var_47.unsqueeze(2), torch.tensor([1, 1, poly_size])), cse_var_49, cse_var_73) , where(cse_var_47, cse_var_48, cse_var_72))
		return l_new, u_new, L_new, U_new
	
